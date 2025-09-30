# 🧪 Calculating the Net Charge of Insulin Using Python Lists and Loops

## Lab Overview

In the **Flow Control** module, you learned about `if-else` statements, `while` loops, lists, and `for` loops. Now you will apply what you have learned to a **real-world application**: calculating the net charge of human insulin across different pH levels.

In this lab, you will:

* Create a **dictionary of pKa values** used in net charge calculations
* Use the `count()` method to calculate amino acid counts
* Use a **while loop** to calculate the net charge of insulin from pH 0 to pH 14

**Estimated completion time:** 25 minutes

---

## 🔑 Step 1: Accessing the AWS Cloud9 IDE

1. Start your lab environment by choosing **Start Lab**.
2. Wait until you see **Lab status: ready**, then close the Start Lab panel.
3. At the top, choose **AWS**.

   * The AWS Management Console opens in a new browser tab.
   * You are logged in automatically.

⚠️ If a new tab does not open, allow pop-ups in your browser.

4. In the AWS console, go to **Services > Cloud9**.
5. Under **Your environments**, locate `reStart-python-cloud9` and select **Open IDE**.

---

## 📂 Step 2: Creating Your Python Exercise File

1. From the menu bar, choose **File > New From Template > Python File**.
2. Delete the sample code.
3. Save the file as `net-charge.py` under `/home/ec2-user/environment`.

---

## 💻 Step 3: Accessing the Terminal

1. In Cloud9, choose **+ → New Terminal**.
2. Verify your working directory with:

```bash
pwd
```

This should display:

```
/home/ec2-user/environment
```

---

## 🧩 Exercise 1: Assigning Variables, Lists, and Dictionaries

Paste the following code into your file:

```python
# Python3.6
# Coding: utf-8

# Store the human preproinsulin sequence
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store sequence elements of human insulin
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin  = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin  = "giveqcctsicslyqlenycn"
cInsulin  = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

# Dictionary of amino acids that contribute to net charge
pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}
```

---

## 🧩 Exercise 2: Counting Amino Acids

Use the `count()` method to calculate how many times each amino acid appears:

```python
# Example: count Y amino acids
insulin.count("y")

# Cast to float
float(insulin.count("y"))

# Count all relevant amino acids using list comprehension
seqCount = {x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']}
```

---

## 🧩 Exercise 3: Writing the Net Charge Formula

Now, calculate the net charge from **pH 0 to pH 14**.

```python
pH = 0

while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) 
              for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) 
              for x in ['y','c','d','e']}.values()))
    )

    print('{0:.2f}'.format(pH), netCharge)
    pH += 1
```

---

## ⚠️ Important: Python Indentation

* Ensure that everything inside the **while loop** is indented correctly.
* Even one misplaced space will cause errors.

---

## ✅ Completion

You’ve now used **lists, dictionaries, loops, and basic math** in Python to compute the net charge of insulin across different pH levels.

🎉 Congratulations—you’ve completed the lab!
