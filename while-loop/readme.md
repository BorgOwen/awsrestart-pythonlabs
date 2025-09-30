# Working with Loops

## Lab Overview

A **loop** is a segment of code that repeats until a condition is met.
In this lab, you will explore two common types of loops:

* `while` loop
* `for` loop

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
* Save it as `while-loop.py` in `/home/ec2-user/environment`.

---

### 2. Open the Terminal

* Open a new terminal in Cloud9.
* Confirm you’re in `/home/ec2-user/environment` with:

  ```bash
  pwd
  ```

---

### 3. Exercise 1: Working with a `while` Loop

#### Print Game Rules

```python
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
```

#### Import Random Module and Generate Number

```python
import random

number = random.randint(1, 10)
isGuessRight = False
```

#### Create the `while` Loop

```python
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
```

**Notes:**

* The loop continues until `isGuessRight` is set to `True`.
* Indentation in Python defines which statements belong to the loop.

#### Pseudocode Example

* If the user has not guessed correctly, repeat:

  * Ask for a guess.
  * If correct → congratulate and exit loop.
  * If incorrect → tell them to try again.

---

### 4. Add Comments

Use comments (`#`) to document your code and explain what each part does.

---

### 5. Exercise 2: Working with a `for` Loop

#### Create New Python File

* Create a new file named `for-loop.py`.
* Add the following:

```python
print("Count to 10!")
```

#### Write the `for` Loop

```python
for x in range(0, 11):
    print(x)
```

**Explanation:**

* `range(0, 11)` generates numbers from 0 through 10 (ending number is not inclusive).
* Each loop assigns the next number in the sequence to `x` and prints it.

---

## End of Lab

Congratulations! You have worked with **`while` loops** and **`for` loops** in Python.
