# Working with the String Data Type

## Lab Overview

In Python, a collection of letters and symbols is called a **string**. Strings are commonly used for input and output.

### What you will learn

* Write Python code that uses the string data type
* Concatenate strings
* Use strings to get input
* Format strings for output

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
* Save it as `string-data-type.py` in `/home/ec2-user/environment`.

---

### 2. Open the Terminal

* Open a new terminal in Cloud9.
* Confirm you’re in `/home/ec2-user/environment` with:

  ```bash
  pwd
  ```

---

### 3. Exercise 1: Introducing the String Data Type

Create a script:

```python
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
```

Run it:

```bash
python3 string-data-type.py
```

**Expected Output:**

```
This is a string.
<class 'str'>
This is a string. is of the data type <class 'str'>
```

---

### 4. Exercise 2: String Concatenation

```python
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
```

**Expected Output:**

```
waterfall
```

---

### 5. Exercise 3: Working with Input Strings

```python
name = input("What is your name? ")
print(name)
```

**Example Run:**

```
What is your name? Maria
Maria
```

---

### 6. Exercise 4: Formatting Output Strings

```python
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))
```

**Example Run:**

```
What is your name? Maria
Maria
What is your favorite color? blue
What is your favorite animal? dog
Maria, you like a blue dog!
```

---

## End of Lab

Congratulations! You have used Python to:

* Concatenate strings
* Take input from the user
* Output a formatted string

