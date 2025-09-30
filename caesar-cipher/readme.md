# 🔐 Using Functions to Implement a Caesar Cipher

## Lab Overview

In programming, a **function** is a named section of code that performs a specific task.

* Python includes built-in functions like `print()`.
* You can also import functions from other modules (e.g., `math.floor()` from the `math` module).
* You can even create your own **user-defined functions**.

To explore user-defined functions, you will implement a **Caesar cipher** — a simple encryption method where each letter in a message is shifted along the alphabet by a fixed number of positions.

In this lab, you will:

* Create user-defined functions
* Use multiple functions together to build an encryption program

**Estimated completion time:** 60 minutes

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
3. Save the file as `caesar-cipher.py` under `/home/ec2-user/environment`.

---

## 💻 Step 3: Accessing the Terminal

1. In Cloud9, choose **+ → New Terminal**.
2. Verify your working directory with:

```bash
pwd
```

Expected output:

```
/home/ec2-user/environment
```

---

## 🧩 Exercise 1: Creating a User-Defined Function

Define a function that **doubles an alphabet string**:

```python
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
```

✅ Example:
Input: `"ABC"` → Output: `"ABCABC"`

---

## 🧩 Exercise 2: Getting a Message

Create a function that prompts the user for a message:

```python
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
```

---

## 🧩 Exercise 3: Getting a Cipher Key

The cipher key determines how far to shift letters (between 1–25).

```python
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount
```

---

## 🧩 Exercise 4: Encrypting a Message

Write a function to encrypt a message:

```python
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter
    return encryptedMessage
```

---

## 🧩 Exercise 5: Decrypting a Message

Reuse your encryption function by reversing the key:

```python
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
```

---

## 🧩 Exercise 6: Creating the Main Program

Bring it all together:

```python
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f"Alphabet: {myAlphabet}")
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f"Alphabet2: {myAlphabet2}")
    
    myMessage = getMessage()
    print(myMessage)
    
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f"Encrypted Message: {myEncryptedMessage}")
    
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f"Decrypted Message: {myDecryptedMessage}")
```

At the end of your file, **call the function**:

```python
runCaesarCipherProgram()
```

---

## 📝 Example Run

```
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
Please enter a message to encrypt: new message
new message
Please enter a key (whole number from 1-25): 4
4
Encrypted Message: RIA QIWWEKI
Decrypted Message: NEW MESSAGE
```

---

## ✅ Completion

Congratulations! You have:

* Created user-defined functions
* Combined them into a working Caesar cipher encryption program 🎉
