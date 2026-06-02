# NoSQL and MongoDB Research

## Introduction
Databases are used to store, organise, and manage data efficiently. NoSQL databases were created to handle large amounts of unstructured or flexible data that traditional relational databases may struggle with.

MongoDB is a document database that stores JSON-like documents, allowing flexible schema design alongside powerful querying and aggregation tools for data analysis.

## What is NoSQL?
- Non-relational database
- Flexible schema
- Horizontal scaling
- High performance for large datasets

### Types of NoSQL Databases
- Document databases
- Key-value databases
- Column-family databases
- Graph databases

## SQL vs NoSQL

| SQL | NoSQL |
|------|------|
| Relational | Non-relational |
| Fixed schema | Flexible schema |
| Tables & rows | Documents |
| Vertical scaling | Horizontal scaling |

## What is MongoDB?
MongoDB is a document-oriented NoSQL database designed to store flexible JSON-like documents called BSON documents.

### Key Features of MongoDB
- BSON documents
- Collections
- Flexible schema
- Fast querying
- Scalability
- Replication

## Advantages of MongoDB
- Open source
  - Publicly available
  - Can be modified and distributed freely
- Flexible schema
  - Different document structures can exist in the same collection
- Horizontal scaling
  - Easier to scale large applications across multiple servers
- High performance
  - Fast read and write operations for large datasets
- Good for unstructured data
  - Handles JSON-style and changing data effectively

## Disadvantages of MongoDB
- Higher memory usage and possible data redundancy
- Can become inconsistent if data is not structured carefully
- Less strict relationships compared to SQL databases
- Transactions are more limited compared to relational databases

## Common Use Cases for MongoDB
- Social media data and posts
- API and JSON data
- Mobile application backends
- Caching systems
- Product information
- CMS and CRM systems
- IoT and sensor data
- Logs and monitoring data
- Gaming data

## MongoDB Structure

### Database
Contains collections.

### Collection
Equivalent to a SQL table.

### Document
Equivalent to a SQL row.

Example:
```json
{
  "name": "Charlie",
  "age": 33,
  "role": "Data Engineer"
}
```

## Connecting to MongoDB Locally Using Compass

MongoDB Compass is MongoDB’s graphical user interface used to manage databases visually. After starting the MongoDB server locally, Compass can connect using:

```mongosh
mongodb://localhost:27017
```

This allows databases, collections, and documents to be viewed and managed without using only the terminal.

## MongoShell

By default, mongosh opens using the `test` database.

We can create and switch to a new database using the `use` command:

```mongosh
use sparta
```

## Creating a New Collection

We can create a new collection called `institute` to store related documents:

```mongosh
db.createCollection("institute")
```

## Adding a Document

To insert a single document into the collection:

```mongosh
db.institute.insertOne({
  name: "New document"
})
```

## Adding Multiple Documents

We can insert multiple documents in one command using `insertMany()`:

```mongosh
db.institute.insertMany([
  {"course": "Data Engineering"},
  {"course": "Data Analysis"}
])
```

## Viewing Documents

To view all documents inside a collection:

```mongosh
db.institute.find()
```

## Example Document

```mongosh
db.institute.insertOne({
  name: "Charlie Warburg",
  age: 33,
  role: "Data Engineering Student",
  location: "London",
  skills: ["SQL", "Python", "MongoDB"],
  previousExperience: "Senior Product Designer"
})
```

# Further Work

## 1. What is Validation?

Validation in MongoDB is used to control the structure and quality of the data being inserted into a collection.

It allows us to define rules for documents, such as:

- Required fields
- Data types
- Minimum or maximum values
- Patterns for strings

### Example

```js
db.createCollection("students", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "age", "course"],
      properties: {
        name: {
          bsonType: "string",
          description: "Name must be a string"
        },
        age: {
          bsonType: "int",
          minimum: 18,
          description: "Age must be an integer and at least 18"
        },
        course: {
          bsonType: "string",
          description: "Course must be a string"
        }
      }
    }
  },
  validationAction: "error"
})
```

## Invalid Example

```
db.students.insertOne({
  name: "Charlie",
  age: "twenty",
  course: "MongoDB"
})
```

### Output
```
MongoServerError: Document failed validation
```

## Valid Example

```
db.students.insertOne({
  name: "Charlie",
  age: 20,
  course: "MongoDB"
})
```

### Output
```
{
  acknowledged: true,
  insertedId: ObjectId('6a1da91c6d15950f844f2e77')
}
```

## 2. Searching for Documents with Mongosh

For this task, I created a collection called `films` to store data about my favourite films.

### Create Collection with Validation

```js
db.createCollection("films", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["title", "director", "year", "genre", "rating"],
      properties: {
        title: {
          bsonType: "string",
          description: "Title must be a string and is required"
        },
        director: {
          bsonType: "string",
          description: "Director must be a string and is required"
        },
        year: {
          bsonType: "int",
          minimum: 1900,
          maximum: 2100,
          description: "Year must be an integer"
        },
        genre: {
          bsonType: "string",
          description: "Genre must be a string"
        },
        rating: {
          bsonType: "double",
          minimum: 0,
          maximum: 10,
          description: "Rating must be a number between 0 and 10"
        }
      }
    }
  },
  validationAction: "error"
})
```

This creates a `films` collection with validation rules to ensure documents follow the correct structure and data types.

### Insert One Document

```js
db.films.insertOne({
  title: "Dune",
  director: "Denis Villeneuve",
  year: 2021,
  genre: "Sci-Fi",
  rating: 8.0
})
```

This inserts a single film document into the collection.

### Insert Many Documents

```js
db.films.insertMany([
  {
    title: "Blade Runner 2049",
    director: "Denis Villeneuve",
    year: 2017,
    genre: "Sci-Fi",
    rating: 8.0
  },
  {
    title: "The Dark Knight",
    director: "Christopher Nolan",
    year: 2008,
    genre: "Action",
    rating: 9.0
  },
  {
    title: "Spirited Away",
    director: "Hayao Miyazaki",
    year: 2001,
    genre: "Animation",
    rating: 8.6
  },
  {
    title: "Interstellar",
    director: "Christopher Nolan",
    year: 2014,
    genre: "Sci-Fi",
    rating: 8.7
  }
])
```

This inserts multiple film documents at once using `insertMany()`.

### Searching for Documents

```js
db.films.find()
```

This returns all documents inside the `films` collection.

```js
db.films.findOne({ title: "Dune" })
```

This searches for a single document where the title is `"Dune"`.

```js
db.films.find({ genre: "Sci-Fi" })
```

This returns all films with the genre `"Sci-Fi"`.

### Bonus: insert()

```js
db.films.insert({
  title: "Inception",
  director: "Christopher Nolan",
  year: 2010,
  genre: "Sci-Fi",
  rating: 8.8
})
```

`insert()` is an older MongoDB method used to insert documents. `insertOne()` and `insertMany()` are preferred because they are clearer and more modern.

### Update an Existing Document

```js
db.films.updateOne(
  { title: "Dune" },
  { $set: { rating: 8.2 } }
)
```

This updates the rating value for the film `"Dune"`.

### Update Multiple Documents

```js
db.films.updateMany(
  { genre: "Sci-Fi" },
  { $set: { recommended: true } }
)
```

This updates all Sci-Fi films and adds a `recommended` field.

### Delete a Document

```js
db.films.deleteOne({
  title: "Inception"
})
```

This deletes the first document that matches the title `"Inception"`.

### Delete Multiple Documents

```js
db.films.deleteMany({
  genre: "Sci-Fi"
})
```

This deletes all documents with the genre `"Sci-Fi"`.

---

# 3. Research Embedding vs Referencing in MongoDB

## What is Embedding in MongoDB?

Embedding means storing related data inside the same document.

For example, an order document may contain customer information and product details inside a single document rather than splitting them into separate collections.

### Why Use Embedding?
- Faster reads because related data is stored together
- Fewer queries are needed
- Easier to retrieve complete related information
- Good for one-to-one or one-to-few relationships

### Embedding Example

```json
{
  "customer": "Charlie",
  "products": [
    {
      "name": "Keyboard",
      "price": 100
    },
    {
      "name": "Mouse",
      "price": 40
    }
  ]
}
```

This stores products directly inside the customer order document.

---

## What is Referencing in MongoDB?

Referencing means storing related data in separate collections and linking them together using IDs.

For example, customer data may exist in one collection while orders exist in another collection connected by a customer ID.

### Why Use Referencing?
- Reduces duplicated data
- Better for large or complex datasets
- Easier to update shared information
- Good for one-to-many or many-to-many relationships

### Referencing Example

### Customers Collection

```json
{
  "_id": 1,
  "name": "Charlie"
}
```

### Orders Collection

```json
{
  "customerId": 1,
  "product": "Keyboard"
}
```

This links the order to the customer using the `customerId` field.

---

## Embedding vs Referencing Summary

| Embedding | Referencing |
|---|---|
| Stores related data together | Stores related data separately |
| Faster reads | Better for complex relationships |
| Can duplicate data | Reduces duplication |
| Good for smaller related datasets | Good for large scalable systems |
| Simpler queries | More flexible structure |