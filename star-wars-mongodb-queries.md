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