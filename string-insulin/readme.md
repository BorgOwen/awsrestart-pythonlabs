# Working with the String Sequence and Numeric Weight of Insulin in Python

## Lab Overview

In the **Python Basics** module, you learned about variables, comments, math, concatenations, and exceptions.
In this lab, you will apply those skills to the real-world example of **human insulin**.

You will:

* Store the protein sequence of human preproinsulin in a **string variable**
* Store the weight of preproinsulin in **int** and **float** variables
* Print these variables with comments explaining the code
* Perform basic math and string concatenations

**Estimated completion time:** 30 minutes

---

## Objectives

By the end of this lab, you will:

* Add comments explaining your code’s flow
* Use `print()` to display code output in the console
* Manipulate strings to extract insulin from preproinsulin
* Perform math on the molecular weight and sequence
* Assign variables of type `string`, `int`, and `float`
* Explore Python exceptions

---

## Prerequisites

You’ll use the **AWS Cloud9 IDE** in this lab.

1. Start the lab and wait for **Lab status: ready**.
2. In the AWS Console, open **Cloud9** and select your environment (`reStart-python-cloud9`).
3. Open the IDE and dismiss any pop-ups.

---

## Steps

### 1. Create Your Python Exercise File

* In Cloud9, go to **File > New From Template > Python File**.
* Remove the sample code.
* Save the file as `string-insulin.py` in `/home/ec2-user/environment`.

---

### 2. Open the Terminal

* Open a new terminal in Cloud9.
* Confirm you’re in `/home/ec2-user/environment` with:

  ```bash
  pwd
  ```

---

### 3. Exercise 1: Assign Variables to Insulin Sequences

1. Open the file `string-insulin.py`.

2. Always begin with comments. For example:

   ```python
   #!/usr/bin/env python3.6
   # coding: utf-8
   ```

3. Add a note:

   ```python
   # Store the human preproinsulin sequence in a variable called preproInsulin
   ```

4. Define the first variable:

   ```python
   preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
   "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
   ```

   *Note:* The backslash (`\`) ensures compliance with PEP 8 (max 79 characters per line).

5. Define the remaining sequences:

   ```python
   # Store the remaining sequence elements of human insulin in variables:
   lsInsulin = "malwmrllpllallalwgpdpaaa"
   bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
   aInsulin = "giveqcctsicslyqlenycn"
   cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
   ```

6. Merge smaller sequences:

   ```python
   insulin = bInsulin + aInsulin
   ```

---

### 4. Exercise 2: Print Sequences with `print()`

1. Add a note:

   ```python
   # Printing the sequence of human insulin
   ```
2. Print preproinsulin:

   ```python
   print("The sequence of human preproinsulin:")
   print(preproInsulin)
   ```
3. Print using concatenation:

   ```python
   print("The sequence of human insulin, chain a: " + aInsulin)
   ```
4. Or with multiple arguments:

   ```python
   print("The sequence of human insulin, chain a:", aInsulin)
   ```

---

### 5. Exercise 3: Calculate the Rough Molecular Weight of Insulin

Add this code to the bottom of your script:

```python
# Calculating the molecular weight of insulin
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Count amino acids in the insulin sequence
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in aaWeights})

# Multiply count by weights
molecularWeightInsulin = sum({x: (aaCountInsulin[x] * aaWeights[x]) for x in aaWeights}.values())

print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
```

---

### 6. Exercise 4: Compare with the Actual Weight

```python
molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
```

*Note:* The program calculates ~6696.42 because it ignores bonds and post-translational processing.
The actual molecular weight is **5807.63**.

---

## Conclusion

You created variables, used `print()`, concatenated strings, and calculated the molecular weight of insulin.
This sets the stage for working with **loops and functions** in later labs.
