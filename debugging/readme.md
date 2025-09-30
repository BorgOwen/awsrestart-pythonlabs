# 🐛 Debugging the Caesar Cipher Program

## Lab Overview

A **debugger** is a tool to test and find bugs in programs. In this lab, you’ll use **Python Debugger (pdb)** to fix buggy Caesar Cipher programs.

You will:

* Use the Python Debugger
* Debug 4 different buggy Caesar Cipher programs

**Estimated time:** 60 minutes

---

## 🔑 Step 1: Access AWS Cloud9 IDE

1. Start the lab → choose **Start Lab**.
2. Wait for **Lab status: ready**.
3. Open the AWS Console → go to **Services > Cloud9**.
4. Open the `reStart-python-cloud9` IDE.

---

## 📂 Step 2: Create Your Python File

1. **File > New From Template > Python File**
2. Delete sample code.
3. Save as:

   * `debug-caesar-1.py`
   * Location: `/home/ec2-user/environment`

---

# 🧩 Exercise 1 – Buggy Caesar Cipher #1

### Code Behavior:

When you run, you’ll see this error:

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Bug:

`cipherKey` is returned as a string, but the program tries to add it to an integer.

### Fix:

Convert `cipherKey` to an integer in `getCipherKey()` or inside `encryptMessage()`.

---

# 🧩 Exercise 2 – Buggy Caesar Cipher #2

### Code Behavior:

Runs without crashing, but **only partially encrypts** the message:

```
Encrypted Message: CYU Testart rocks!
```

### Bug:

The message isn’t converted to uppercase before encryption, so lowercase letters are skipped.

### Fix:

Update `uppercaseMessage = message.upper()` instead of `uppercaseMessage = message`.

---

# 🧩 Exercise 3 – Buggy Caesar Cipher #3

### Code Behavior:

Encryption works, but **decryption is wrong**:

```
Encrypted Message: CYU TGUVCTV TQEMU!
Decrypted Message: EAW VIWXEVX VSGOW!
```

### Bug:

In `decryptMessage()`, the wrong variable is passed.

```python
# Wrong
return encryptMessage(message, cipherKey, alphabet)

# Correct
return encryptMessage(message, decryptKey, alphabet)
```

---

# 🧩 Exercise 4 – Buggy Caesar Cipher #4

### Code Behavior:

Decryption just returns the encrypted text again:

```
Encrypted Message: CYU TGUVCTV TQEMU!
Decrypted Message: CYU TGUVCTV TQEMU!
```

### Bug:

In `runCaesarCipherProgram()`, the **wrong variable is printed** for the decrypted message.

```python
# Wrong
print(f'Decrypted Message: {myEncryptedMessage}')

# Correct
print(f'Decrypted Message: {myDecryptedMessage}')
```

---

## 🎉 Completion

You successfully:

* Debugged 4 broken Caesar Cipher versions
* Practiced `pdb` and step-through debugging
* Fixed type errors, case-sensitivity issues, wrong variables, and incorrect prints

**Congrats — you’ve finished all the labs for this course!**
