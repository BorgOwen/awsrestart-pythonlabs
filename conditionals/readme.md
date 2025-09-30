# Working with Conditionals

## Lab Overview

A **conditional statement** is a piece of code that compares two pieces of information to decide what happens next.
It’s how programs make decisions and take different paths.

In this lab, you will:

* Use the `if` statement
* Use the `else` statement
* Use the `elif` statement

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
* Save it as `conditionals.py` in `/home/ec2-user/environment`.

---

### 2. Open the Terminal

* Open a new terminal in Cloud9.
* Confirm you’re in `/home/ec2-user/environment` with:

  ```bash
  pwd
  ```

---

### 3. Exercise 1: Using the `if` Statement

Edit your Python file to ship packages:

```python
userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")
```

* Save and run the file.
* Try entering `yes` → you should see a response.
* Try entering `no` → the program exits with no output.

---

### 4. Exercise 2: Using the `else` Statement

Improve customer service by adding a response for “no”:

```python
userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
```

* Save and run the file.
* Enter `no` → see the polite response.
* Enter `yes` → see the shipping response.

---

### 5. Exercise 3: Using the `elif` Statement

Offer additional services:

```python
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
```

* Save and run the file.
* Test different inputs: `stamps`, `envelope`, `copy`, `no`.

**Note:** Only one condition runs each time. Once a condition is true, the rest are skipped.

---

## End of Lab

Congratulations! You have written a Python script that uses **if, elif, and else** statements to make decisions.

