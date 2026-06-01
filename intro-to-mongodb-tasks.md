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