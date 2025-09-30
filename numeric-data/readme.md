# Working with Numeric Data Types

## Lab Overview

Python makes it easier to work with math. It’s one of the most popular languages among data scientists who analyze large amounts of data. In this lab, you’ll explore the basic data types used to store numeric values.

### What you will learn

* Using the Python shell
* Working with the `int` data type
* Working with the `float` data type
* Working with the `complex` data type
* Working with the `bool` data type

**Estimated completion time:** 60 minutes

---

## Prerequisites

You’ll use the **AWS Cloud9 IDE** for this lab.

1. Start the lab environment and wait until you see **Lab status: ready**.
2. In the AWS Console, open **Cloud9** and choose your environment (`reStart-python-cloud9`).
3. Open the IDE and dismiss any pop-ups.

---

## Steps

### 1. Create Your Python Exercise File

* In Cloud9, go to **File > New From Template > Python File**.
* Save it as `numeric-data.py` in `/home/ec2-user/environment`.

---

### 2. Open the Terminal

* Open a new terminal in Cloud9.
* Confirm you’re in `/home/ec2-user/environment` with:

  ```bash
  pwd
  ```

---

### 3. Exercise 1: Using the Python Shell

Start Python:

```bash
python3
```

Try basic math:

```python
2 + 2    # Output: 4
4 - 2    # Output: 2
2 * 2    # Output: 4
4 / 2    # Output: 2.0
```

Exit the shell with:

```python
quit()
```

---

### 4. Exercise 2: `int` Data Type

Edit your file:

```python
print("Python has three numeric types: int, float, and complex")

myValue = 1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
```

Run it:

```bash
python3 numeric-data.py
```

---

### 5. Exercise 3: `float` Data Type

```python
myValue = 3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
```

---

### 6. Exercise 4: `complex` Data Type

```python
myValue = 5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
```

---

### 7. Exercise 5: `bool` Data Type

```python
myValue = True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue = False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
```

---

## Expected Output (Sample)

```
Python has three numeric types: int, float, and complex
1
<class 'int'>
1 is of the data type <class 'int'>
3.14
<class 'float'>
3.14 is of the data type <class 'float'>
5j
<class 'complex'>
5j is of the data type <class 'complex'>
True
<class 'bool'>
True is of the data type <class 'bool'>
False
<class 'bool'>
False is of the data type <class 'bool'>
```

---

## 🎉 Completion

You have learned about Python’s three numeric data types: **int, float, complex**, and the additional **bool** type.

