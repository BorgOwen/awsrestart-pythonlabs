# Preparing to Analyze Insulin with Python

## Lab Overview

Python is a flexible programming language often used in scientific computing for handling strings, sequences, and numbers.
In this lab, you’ll perform sequence manipulations and calculations on **human insulin**, a hormone that regulates blood sugar.

**Estimated completion time:** 30 minutes

---

## Objectives

By the end of this lab, you will:

* Retrieve the protein sequence of **human preproinsulin**
* Prepare and clean the data for further processing

---

## Prerequisites

You’ll use the **AWS Cloud9 IDE** in this lab.

1. Start your lab environment and wait until the status shows **Lab status: ready**.
2. In the AWS Console, open **Cloud9** and choose your environment (`reStart-python-cloud9`).
3. Open the IDE and close any pop-ups.

---

## Steps

### 1. Create a Python Exercise File

* In Cloud9, choose **File > New From Template > Python File**.
* Remove the sample code.
* Save the file as `analyze-insulin.py` under `/home/ec2-user/environment`.

---

### 2. Open a Terminal Session

* In Cloud9, choose **+ > New Terminal**.
* Confirm your working directory with:

  ```bash
  pwd
  ```

  It should point to `/home/ec2-user/environment`.

---

### 3. Exercise 1: Retrieve the Protein Sequence of Human Preproinsulin

* Go to [NCBI](https://ncbi.nlm.nih.gov).
* From the dropdown menu, select **Protein**.
* Search for **human insulin**.
* Open the result **insulin [Homo sapiens]**.
* Copy the sequence starting with `ORIGIN` and ending with `//`.
* In Cloud9, create a new file named `preproinsulin-seq.txt`.
* Paste the sequence into the file.

---

### Bonus: Clean the Sequence Programmatically

Clean the file `preproinsulin-seq.txt` by removing:

* `ORIGIN`
* Numbers
* `//`
* Spaces and line breaks

Your cleaned file should contain exactly **110 characters**.

---

### 4. Exercise 2: Obtain the Protein Sequence of Human Insulin

Preproinsulin contains:

* A **24aa signal sequence**
* An **86aa proinsulin molecule**

Insulin is made from amino acids:

* **25–54**
* **90–110**

Steps:

1. Clean the sequence manually or programmatically.
2. Save it as `preproinsulin-seq-clean.txt`.
3. Create separate files:

   * `lsinsulin-seq-clean.txt` → amino acids 1–24 (24 characters)
   * `binsulin-seq-clean.txt` → amino acids 25–54 (30 characters)
   * `cinsulin-seq-clean.txt` → amino acids 55–89 (35 characters)
   * `ainsulin-seq-clean.txt` → amino acids 90–110 (21 characters)

---

## Reflection: Automate or Manual?

Not every task needs automation. For a single sequence, manual cleanup is faster.
For thousands of sequences, automation saves significant time.

---

## Conclusion

You have retrieved and prepared **human preproinsulin sequences** for further analysis. This foundation will help you appreciate the efficiency that Python provides for scientific data processing.
