# Working with Lists, Tuples, and Dictionaries

## Lab Overview

In Python, string and numeric data types are often grouped into collections. Three common collections that Python supports are:

* **List**
* **Tuple**
* **Dictionary**

### What you will learn

* Use the **list** data type
* Use the **tuple** data type
* Use the **dictionary** data type

**Estimated completion time:** 45 minutes

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
* Save it as `collections.py` in `/home/ec2-user/environment`.

---

### 2. Open the Terminal

* Open a new terminal in Cloud9.
* Confirm you’re in `/home/ec2-user/environment` with:

  ```bash
  pwd
  ```

---

### 3. Exercise 1: Working with Lists

#### Define a List

```python
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
```

#### Access a List by Position

```python
print(myFruitList[0])  # apple
print(myFruitList[1])  # banana
print(myFruitList[2])  # cherry
```

#### Change a Value in a List

```python
myFruitList[2] = "orange"
print(myFruitList)
```

**Expected Output (Sample):**

```
['apple', 'banana', 'cherry']
<class 'list'>
apple
banana
cherry
['apple', 'banana', 'orange']
```

---

### 4. Exercise 2: Working with Tuples

#### Define a Tuple

```python
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
```

#### Access a Tuple by Position

```python
print(myFinalAnswerTuple[0])  # apple
print(myFinalAnswerTuple[1])  # banana
print(myFinalAnswerTuple[2])  # pineapple
```

**Expected Output (Sample):**

```
('apple', 'banana', 'pineapple')
<class 'tuple'>
apple
banana
pineapple
```

---

### 5. Exercise 3: Working with Dictionaries

#### Define a Dictionary

```python
myFavoriteFruitDictionary = {
    "Akua": "apple",
    "Saanvi": "banana",
    "Paulo": "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
```

#### Access a Dictionary by Key

```python
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
```

**Expected Output (Sample):**

```
{'Akua': 'apple', 'Saanvi': 'banana', 'Paulo': 'pineapple'}
<class 'dict'>
apple
banana
pineapple
```

---

## End of Lab

Congratulations! You have worked with Python’s **list**, **tuple**, and **dictionary** data types.

