# Star Wars MongoDB Queries

## 1. Create DB and Import Data

### Create Database

```js
use starwars
```

This creates and switches to the `starwars` database.

### Import JSON Files

```bash
cd "~/Downloads/Star Wars Files"

for file in *.json
do
  mongoimport --db starwars --collection people --file "$file" --jsonArray
done
```

This imports all Star Wars character JSON files into the `people` collection.

### Find Luke Skywalker

```js
db.people.findOne({ name: "Luke Skywalker" })
```

This searches for the document containing Luke Skywalker.

---

## 2. Find Particular Fields

```js
db.people.findOne(
  { name: "Luke Skywalker" },
  { name: 1, eye_color: 1, _id: 0 }
)
```

This returns only Luke Skywalker's name and eye colour.

---

## 3. Find Ackbar

```js
db.people.findOne(
  { name: "Ackbar" },
  { name: 1, species: 1, _id: 0 }
)
```

This returns Ackbar's name and species.

---

## 4. All Humans

```js
db.people.find(
  { species: "Human" },
  { name: 1, homeworld: 1, _id: 0 }
)
```

This returns all humans and their homeworlds.

---

## 5. Yellow or Orange Eyes

```js
db.people.find({
  eye_color: { $in: ["yellow", "orange"] }
})
```

This returns all characters with yellow or orange eyes.

---

## 6. Tall Characters

```js
db.people.find({
  height: { $gt: "200" }
})
```

This returns all characters with a height greater than 200.

---

# 7. Experiment with Operators

## $eq

```js
db.people.find({
  gender: { $eq: "male" }
})
```

Returns documents where gender equals `"male"`.

---

## $gt

```js
db.people.find({
  height: { $gt: "180" }
})
```

Returns documents where height is greater than 180.

---

## $gte

```js
db.people.find({
  height: { $gte: "180" }
})
```

Returns documents where height is greater than or equal to 180.

---

## $in

```js
db.people.find({
  eye_color: { $in: ["blue", "yellow"] }
})
```

Returns documents where eye colour is blue or yellow.

---

## $lt

```js
db.people.find({
  height: { $lt: "170" }
})
```

Returns documents where height is less than 170.

---

## $lte

```js
db.people.find({
  height: { $lte: "170" }
})
```

Returns documents where height is less than or equal to 170.

---

## $ne

```js
db.people.find({
  gender: { $ne: "male" }
})
```

Returns documents where gender is not `"male"`.

---

## $nin

```js
db.people.find({
  eye_color: { $nin: ["blue", "brown"] }
})
```

Returns documents where eye colour is not blue or brown.

## $and

```js
db.people.find(
  {
    $and: [
      {eye_color: "blue"},
      {gender: "female"},
    ]
  },
  {
    name: 1,
    eye_color: 1,
    gender: 1,
    _id: 0
  }
)
```

This returns characters who are female and have blue eyes.

## $or

```js
db.people.find(
  {
    $or: [
      {eye_color: "blue"},
      {gender: "female"},
    ]
  },
  {
    name: 1,
    eye_color: 1,
    gender: 1,
    _id: 0
  }
)
```

This returns characters who either have blue eyes or are female.

## Aggregation and Data Type Conversion

The problem I had was that `height` was stored as a string instead of an integer. This meant MongoDB could not reliably perform mathematical operations such as `$sum` or `$max` until the value was converted.

There was also another issue: some height values were stored as `"unknown"`, which cannot be converted into a number.

### Option 1: Remove Unknown Heights, Then Convert

```js
db.people.updateMany(
  { height: "unknown" },
  { $unset: { height: "" } }
)

db.people.updateMany(
  {},
  [
    { $set: { height: { $toInt: "$height" } } }
  ]
)
```

This removes the `height` field where the value is `"unknown"`, then permanently converts the remaining height values from strings into integers.

### Option 2: Convert Only Valid Numeric Heights

```js
db.people.update(
  { height: /^[0-9]+$/ },
  [
    { $set: { height: { $toInt: "$height" } } }
  ],
  { multi: true }
)
```

This uses regex to only select documents where `height` contains numbers, then permanently converts those valid height values into integers.

### My Non-Destructive Solution

```js
db.people.aggregate([
  {
    $group: {
      _id: "$homeworld.name",
      maxHeight: {
        $max: {
          $convert: {
            input: "$height",
            to: "int",
            onError: null,
            onNull: null
          }
        }
      }
    }
  }
])
```

This finds the maximum height per homeworld. I used `$convert` inside the aggregation because it is non-destructive: it temporarily converts `height` to an integer during the query without changing the original data in the database.

The `onError: null` part handles values like `"unknown"` by turning them into `null`, so they are ignored in the calculation instead of crashing the query.

### All Human Heights Summed

```js
db.people.aggregate([
  { $match: { "species.name": "Human" } },
  { $group: { _id: null, total: { $sum: "$height" } } }
])
```

This sums the height values for all human characters. This only works correctly after height has been converted into a numeric data type.

### All Human Heights Summed and Grouped by Gender

```js
db.people.aggregate([
  { $match: { "species.name": "Human" } },
  { $group: { _id: "$gender", total: { $sum: "$height" } } }
])
```

This groups human characters by gender and sums the height values for each group.

### Find All Species Names

```js
db.people.distinct("species.name")
```

This returns a list of unique species names in the collection.

### Count All Documents

```js
db.people.countDocuments({})
```

This counts all documents in the `people` collection.

### Count All Human Characters

```js
db.people.countDocuments({ "species.name": "Human" })
```

This counts how many characters have the species name `"Human"`.

## Referencing Example

```js
db.createCollection("starships")

db.people.findOne(
  { name: "Darth Vader" },
  { _id: 1, name: 1 }
)

db.starships.insertOne({
  name: "TIE Advanced x1",
  model: "Twin Ion Engine Advanced x1",
  manufacturer: "Sienar Fleet Systems",
  length: 9.2,
  max_atmosphering_speed: 1200,
  crew: 1,
  passengers: 0,
  pilot: ObjectId("6a1e8aed78130100481b6796")
})
```

This demonstrates referencing in MongoDB using `ObjectId`.

First, Darth Vader’s `_id` was retrieved from the `people` collection. That `_id` was then stored inside the `starships` collection as the `pilot` field.

This creates a relationship between the `people` and `starships` collections without duplicating the character data.