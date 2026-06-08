# PySpark Iris Tasks

## Task 1 - Display the Iris DataFrame

```python
iris.show()
```

![Task 1 Output](images/task1output.png)

---

## Task 2 - Display Data Types

```python
iris.dtypes
```

![Task 2 Output](images/task2output.png)

---

## Task 3 - Display Column Names

```python
iris.columns
```

![Task 3 Output](images/task3output.png)

---

## Task 4 - Generate Summary Statistics

```python
iris.describe().show()
```

![Task 4 Output](images/task4output.png)

---

## Task 5 - Select the sepal_length Column

```python
iris.select("sepal_length").show()
```

![Task 5 Output](images/task5output.png)

---

## Task 6 - Display Distinct Species

```python
iris.select("species").distinct().show()
```

![Task 6 Output](images/task6output.png)

---

## Task 7 - Drop the species Column

```python
iris_no_species = iris.drop("species")
iris_no_species.show()
```

![Task 7 Output](images/task7output.png)

---

## Task 8 - Filter Rows Where sepal_length > 5.5

```python
iris.filter(col("sepal_length") > 5.5).show()
```

![Task 8 Output](images/task8output.png)

---

## Task 9 - Filter Species Beginning with "v"

```python
iris.filter(col("species").like("v%")).show()
```

![Task 9 Output](images/task9output.png)

---

## Task 10 - Group by Species and Aggregate Values

```python
iris.groupBy("species").agg(
    avg("sepal_width"),
    max("sepal_length")
).show()
```

![Task 10 Output](images/task10output.png)

---

## Task 11 - Replace Species Names with Initials

```python
iris_initials = iris.withColumn(
    "species",
    when(col("species") == "virginica", "VI")
    .when(col("species") == "versicolor", "VE")
    .when(col("species") == "setosa", "SE")
)

iris_initials.show()
```

![Task 11 Output](images/task11output.png)

---

## Task 12 - Create Missing Values and Remove Null Rows

```python
irisna = iris.replace(0.2, None)

irisna.dropna().show()
```

![Task 12 Output](images/task12output.png)