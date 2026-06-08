# Databricks & Modern Data Engineering Notes

## CI/CD

**CI/CD** stands for **Continuous Integration** and **Continuous Deployment (or Delivery)**.

### Continuous Integration (CI)
Developers regularly merge code changes into a shared repository where automated tests run.

Benefits:
- Faster development cycles
- Early bug detection
- Improved code quality
- Reduced integration issues

### Continuous Deployment (CD)
Once code passes testing, it can be automatically deployed to production.

Benefits:
- Faster releases
- Reduced manual work
- More reliable deployments

---

# ETL vs ELT

## ETL (Extract → Transform → Load)

Data is transformed before being loaded into the destination system.

### Process
1. Extract data from sources
2. Transform and clean data
3. Load into a data warehouse

### Example
```text
CSV → Data Cleaning → Data Warehouse
```

### Best For
- Traditional data warehouses
- Structured data
- Smaller datasets

---

## ELT (Extract → Load → Transform)

Data is loaded first and transformed later inside the target platform.

### Process
1. Extract data
2. Load raw data
3. Transform when needed

### Example
```text
CSV/API → Data Lake → Databricks/Spark Transformations
```

### Best For
- Cloud platforms
- Big data
- Machine Learning
- Analytics workloads

Modern platforms such as Databricks, Snowflake, and BigQuery commonly use ELT.

---

# Relational Data Processing

## OLTP (Online Transaction Processing)

Designed for day-to-day business transactions.

### Characteristics
- Fast inserts and updates
- Thousands of small transactions
- Highly normalised data
- Focus on accuracy and consistency

### Examples
- Banking systems
- E-commerce checkouts
- Booking systems
- CRM systems

### Sample Query
```sql
INSERT INTO Orders (...)
```

Think:

> "Running the business"

---

## OLAP (Online Analytical Processing)

Designed for analysing large volumes of historical data.

### Characteristics
- Complex analytical queries
- Aggregations and reporting
- Large datasets
- Read-heavy workloads

### Examples
- Sales reporting
- Business intelligence dashboards
- Customer behaviour analysis
- Financial forecasting

### Sample Query
```sql
SELECT
    month,
    SUM(revenue)
FROM sales
GROUP BY month
```

Think:

> "Understanding the business"

---

# Data Warehouses vs Data Lakes

## Data Warehouse

A highly structured repository for analytics.

### Characteristics
- Structured data only
- Schema defined before loading
- Optimised for reporting
- Fast SQL queries

### Schema-on-Write

The schema is defined before data is stored.

```text
Data → Validate Structure → Store
```

Examples:
- Snowflake
- Redshift
- BigQuery

---

## Data Lake

A storage system for large amounts of raw data.

### Characteristics
- Structured data
- Semi-structured data
- Unstructured data
- Massive scalability

### Schema-on-Read

Data is stored first.

Schema is applied only when the data is queried.

```text
Store Everything → Apply Structure Later
```

Examples:
- AWS S3
- Azure Data Lake Storage
- Google Cloud Storage

---

## Key Difference

| Feature | Data Warehouse | Data Lake |
|----------|---------------|-----------|
| Schema | Schema-on-Write | Schema-on-Read |
| Data Type | Structured | Any |
| Cost | Higher | Lower |
| Analytics | Fast | Flexible |
| Storage | Processed Data | Raw Data |

---

# What is Databricks?

Databricks is a **cloud-based unified data platform** designed for:

- Data Engineering
- Data Analytics
- Business Intelligence
- Machine Learning
- Artificial Intelligence

It was founded by the creators of:

[Apache Spark](chatgpt://generic-entity?number=0)

---

# Why Databricks Exists

Traditional databases work well until datasets become extremely large.

Eventually, one machine is not enough.

### Problem

A single server can only provide:

- Limited CPU
- Limited RAM
- Limited storage
- Limited processing power

At scale, processing can take hours or even days.

---

## Distributed Computing

Instead of using one machine:

```text
[Server]
```

Use many machines:

```text
[Server] [Server] [Server] [Server] [Server]
```

Large jobs are split into smaller tasks.

```text
Large Job
    ↓
Split into Tasks
    ↓
Distributed Across Cluster
    ↓
Results Combined
```

This is the core idea behind modern big-data systems.

---

# Apache Spark

Spark is the engine that powers Databricks.

Spark performs distributed processing across clusters of machines.

### What Spark Does

- Splits work into smaller tasks
- Executes tasks in parallel
- Reassembles results
- Handles failures automatically

### Why Spark Matters

Instead of:

```text
1 machine doing 1 task
```

You get:

```text
100 machines doing 100 tasks simultaneously
```

This dramatically reduces processing time.

---

# Scaling

## Vertical Scaling

Increase resources on a single machine.

```text
More RAM
More CPU
More Storage
```

Example:

```text
8GB RAM → 64GB RAM
```

Eventually you hit hardware limits.

---

## Horizontal Scaling

Add more machines.

```text
Server + Server + Server + Server
```

Benefits:

- Almost unlimited growth
- Higher resilience
- Better performance

Databricks is built around horizontal scaling.

---

# Cloud Agnostic

Databricks is cloud agnostic.

This means it works on multiple cloud providers.

Examples:

- [Amazon Web Services](chatgpt://generic-entity?number=1)
- [Microsoft Azure](chatgpt://generic-entity?number=2)
- [Google Cloud](chatgpt://generic-entity?number=3)

You are not locked into one provider.

---

# Databricks as a Platform

Traditional databases provide storage.

Databricks provides an entire platform.

### Database

```text
Store Data
Query Data
```

### Databricks

```text
Store Data
Transform Data
Process Data
Train ML Models
Build AI Workloads
Create Dashboards
Manage Pipelines
```

This is why Databricks is considered a:

**Platform as a Service (PaaS)**

---

# Typical Databricks Workflow

Data can arrive from many sources:

```text
CSV Files
APIs
Databases
Streaming Data
IoT Devices
Applications
```

Everything flows into Databricks.

```text
Data Sources
      ↓
Databricks
      ↓
Transformation
      ↓
Storage
      ↓
Analytics / AI / Reporting
```

---

# Notebooks

One of Databricks' most popular features.

A notebook is an interactive workspace made up of cells.

### A Cell Can Contain

- Python
- SQL
- Scala
- R
- Markdown

Example:

```python
df.count()
```

Followed by:

```sql
SELECT * FROM sales
```

Then:

```markdown
# Findings
```

All within the same notebook.

This makes collaboration easier between engineers, analysts, and data scientists.

---

# Spark vs Pandas

## Pandas

Runs on a single machine.

```text
Laptop
↓
Process Data
```

Great for:
- Small datasets
- Quick analysis

---

## Spark

Runs across many machines.

```text
Cluster
↓
Process Data
```

Great for:
- Big data
- Enterprise analytics
- Machine learning pipelines

---

# Delta Lake

Delta Lake is one of the most important technologies within Databricks.

## Definition

Delta Lake is an open-source storage layer that adds reliability and performance to data lakes.

Think of it as:

```text
Data Lake
+
Database Features
=
Delta Lake
```

---

## Why Delta Lake Matters

Traditional data lakes can become:

- Messy
- Inconsistent
- Difficult to trust

Delta Lake introduces:

### ACID Transactions

Ensures data remains reliable.

- Atomicity
- Consistency
- Isolation
- Durability

### Schema Enforcement

Protects against bad data.

### Versioning

Every change is tracked.

You can:

```text
View old versions
Rollback mistakes
Audit changes
```

### Time Travel

Query historical versions of data.

Example:

```sql
SELECT *
FROM sales
VERSION AS OF 10
```

---

# Data Lakehouse

The Lakehouse combines:

### Data Lake

- Cheap storage
- Massive scalability

### Data Warehouse

- Fast analytics
- Governance
- Reliability

Result:

```text
Data Lake
+
Data Warehouse
=
Lakehouse
```

This is the architecture Databricks promotes.

---

# Medallion Architecture

A common data-engineering pattern in Databricks.

Think of it as progressively improving data quality.

---

## Bronze Layer

Raw data.

```text
sales.csv
customer.json
api_response.json
```

Characteristics:
- Untouched
- Original
- Potentially messy

---

## Silver Layer

Cleaned and validated data.

Examples:

- Fixed typos
- Removed duplicates
- Handled null values
- Standardised formats

Characteristics:
- Reliable
- Consistent
- Ready for analysis

---

## Gold Layer

Business-ready data.

Examples:

- Monthly sales reports
- Customer lifetime value
- Revenue dashboards
- Executive reporting datasets

Characteristics:
- Highly refined
- Analytics ready
- Trusted source of truth

---

# Why Databricks is Growing So Fast

Several trends are driving demand:

### Big Data

Organisations collect more data than ever.

### Artificial Intelligence

AI models require huge datasets.

### Machine Learning

Training models often requires distributed processing.

### Cloud Adoption

Businesses continue migrating infrastructure to the cloud.

### Real-Time Analytics

Companies increasingly need immediate insights.

Databricks sits at the centre of all of these trends.

---

# Key Takeaway

The core idea behind Databricks is:

> **Take huge amounts of data, distribute the work across many machines, process it efficiently using Spark, and provide a unified platform for analytics, machine learning, and AI.**

If SQL databases are designed to manage data efficiently on a single system, Databricks is designed to manage and process data efficiently at massive scale across entire clusters of machines.

# What Can Be Considered Big Data?

Big Data refers to datasets that are too large, complex, or fast-moving for traditional databases and processing systems to handle efficiently.

The classic definition is the **5 Vs**:

| V | Meaning |
|----|---------|
| Volume | Massive amounts of data |
| Velocity | Data generated rapidly |
| Variety | Different data types |
| Veracity | Data quality and trustworthiness |
| Value | Ability to extract business value |

## Examples of Big Data

- Netflix viewing data
- TikTok user interactions
- Banking transactions
- IoT sensor streams
- Social media activity
- AI training datasets

A dataset becomes "Big Data" when a single machine can no longer process it efficiently and distributed computing becomes necessary.

---

# ACID

ACID is a set of properties that ensure database transactions remain reliable and accurate.

| Letter | Meaning |
|----------|---------|
| A | Atomicity |
| C | Consistency |
| I | Isolation |
| D | Durability |

## Atomicity

A transaction either succeeds completely or fails completely.

Example:

```text
Transfer £100
↓
Remove from Account A
Add to Account B
```

Both actions happen or neither happens.

## Consistency

The database remains valid before and after the transaction.

Example:

```text
£100 disappears from one account
£100 appears in another
```

Money cannot be lost or created accidentally.

## Isolation

Multiple users can access the database simultaneously without corrupting each other's transactions.

## Durability

Once a transaction has been committed, it remains saved even if the system crashes.

---

# Apache Spark Architecture

Spark uses a distributed architecture to process large datasets across multiple machines.

## Driver Program

The Driver is the brain of the Spark application.

Responsibilities:

- Creates jobs
- Creates tasks
- Coordinates workers
- Tracks execution progress

## Cluster Manager

Responsible for allocating computing resources.

Examples:

- Kubernetes
- YARN
- Standalone Spark Cluster

## Worker Nodes

Machines responsible for performing the actual data processing.

## Executors

Processes running on worker nodes.

Executors:

- Execute tasks
- Store data in memory
- Return results to the Driver

### Simplified Spark Architecture

```text
Driver
   |
Cluster Manager
   |
-------------------------
|          |           |
Worker     Worker     Worker
|           |          |
Executor  Executor  Executor
```

---

# What Problem Did Apache Spark Solve?

Before Spark, many organisations used Apache Hadoop MapReduce.

Hadoop relied heavily on disk-based processing, meaning data was repeatedly written to and read from storage.

```text
Disk → Process → Disk → Process
```

This made large jobs slow.

Spark introduced **in-memory computing**, allowing data to remain in memory during processing.

```text
Memory → Process → Memory
```

This significantly improved performance and reduced processing times.

Benefits included:

- Faster ETL pipelines
- Faster analytics
- Faster machine learning workloads
- Improved scalability

---

# Why Apache Spark Became Popular

## Speed

Much faster than traditional Hadoop MapReduce.

## Multiple Language Support

Supports:

- Python
- Scala
- SQL
- Java
- R

## Unified Processing Engine

Can be used for:

- ETL pipelines
- Streaming data
- Machine Learning
- SQL analytics
- Graph processing

## Scalability

Can run on:

- A laptop
- A cluster of hundreds or thousands of machines

---

# What is PySpark?

PySpark is the Python API for Apache Spark.

It allows developers to use Spark through Python rather than Scala.

## Why We Use PySpark

Most data professionals already know Python.

Benefits include:

- Easier learning curve
- Python ecosystem integration
- Works with Pandas
- Works with NumPy
- Works with Machine Learning libraries

Example:

```python
df = spark.read.csv("sales.csv", header=True)
df.show()
```

PySpark provides the power of Spark while allowing developers to work in a familiar language.

---

# Additional Databricks Features

## Collaborative Notebooks

Multiple users can work together within the same notebook environment.

## Managed Spark Clusters

Databricks automatically manages:

- Infrastructure
- Worker nodes
- Executors
- Scaling

This allows engineers to focus on data rather than server administration.

## Delta Lake Integration

Built directly into the platform to provide reliable and scalable storage.

## Machine Learning Support

Supports:

- MLflow
- Model training
- Experiment tracking
- Model deployment

## SQL Analytics

Allows analysts to query large datasets using SQL.

## Unity Catalog

Provides centralised governance for:

- Data access
- Permissions
- Auditing
- Data lineage

---

# Where to Sign Up for Databricks

Databricks offers a free edition suitable for learning and experimentation.

Website:

https://www.databricks.com/learn/free-edition

---

# Ingesting Data into Databricks

Databricks can ingest data from many sources including:

- CSV files
- JSON files
- Databases
- APIs
- Streaming data
- Cloud storage

## Example: Reading a CSV File

```python
df = spark.read.csv(
    "/FileStore/tables/sales.csv",
    header=True,
    inferSchema=True
)

display(df)
```

## Example: Reading JSON Data

```python
df = spark.read.json(
    "/FileStore/tables/customers.json"
)

display(df)
```

## Example: Reading Parquet Data

```python
df = spark.read.parquet(
    "/FileStore/tables/data.parquet"
)

display(df)
```

---

# Creating a Notebook in Databricks

1. Log into Databricks
2. Navigate to Workspace
3. Click Create
4. Select Notebook
5. Enter a notebook name
6. Select a language:
   - Python
   - SQL
   - Scala
   - R
7. Attach a cluster
8. Begin writing code

Example:

```python
print("Hello Databricks")
```
