# 🧮 Categorizing Values

## Lab Overview

In Python, a list can hold different data types — unlike many other languages where lists are type-specific. In this lab, you’ll create a **mixed-type list** and print out the type of each value.

You will:

* Use numeric data types
* Use string data types
* Use the list data type
* Use a `for` loop
* Use the `print()` function

**Estimated time:** 30 minutes

---

## 🔑 Step 1: Access AWS Cloud9 IDE

1. Start the lab → choose **Start Lab**.
2. Wait for **Lab status: ready**.
3. Open the AWS Console → go to **Services > Cloud9**.
4. Open the `reStart-python-cloud9` IDE.

---

## 📂 Step 2: Create Your Python File

1. **File > New From Template > Python File**
2. Delete the sample code.
3. Save the file as `categorize-values.py` in `/home/ec2-user/environment`.

---

## 💻 Step 3: Open a Terminal

1. In Cloud9, click **+ → New Terminal**.

2. Verify location:

   ```bash
   pwd
   ```

   Output should be:

   ```
   /home/ec2-user/environment
   ```

3. Confirm your `.py` file is in this directory.

---

## 🧩 Exercise – Creating a Mixed-Type List

1. Open your Python file.

2. Add this code:

   ```python
   myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

   for item in myMixedTypeList:
       print("{} is of the data type {}".format(item, type(item)))
   ```

3. Save and run the file.

---

## ✅ Expected Output

You should see:

```
45 is of the data type <class 'int'>
290578 is of the data type <class 'int'>
1.02 is of the data type <class 'float'>
True is of the data type <class 'bool'>
My dog is on the bed. is of the data type <class 'str'>
45 is of the data type <class 'str'>
```

---

## 🎉 Completion

You have:

* Created a list with mixed data types
* Used a `for` loop to traverse it
* Printed each value alongside its data type

This reinforces Python fundamentals from Labs 1–6 — simple but powerful code!
