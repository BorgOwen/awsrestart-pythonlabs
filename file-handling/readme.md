# 💉 Creating File Handlers and Modules for Retrieving Information about Insulin

## Lab Overview

In this lab, you’ll practice **working with files, JSON, and modules in Python**. You’ll store insulin molecule data in JSON, read it with a custom file handler module, and calculate the molecular weight of insulin.

You will:

* Create a **JSON file** with insulin molecule data
* Write a **file handler module** to read JSON
* Parse JSON into Python data structures
* Calculate the molecular weight of insulin

**Estimated time:** 25 minutes

---

## 🔑 Step 1: Access AWS Cloud9 IDE

1. Start the lab → choose **Start Lab**.
2. Wait for **Lab status: ready**.
3. Open the AWS Console → go to **Services > Cloud9**.
4. Open the `reStart-python-cloud9` IDE.

---

## 📂 Step 2: Create Your Files

1. Create a new Python file: **File > New From Template > Python File**

   * Save as `calc_weight_json.py` in `/home/ec2-user/environment`.
2. Create a second file: **File > New File**

   * Save as `jsonFileHandler.py`.
3. Create a directory called `files` to store your JSON data.

---

## 🧬 Step 3: Create the JSON Data File

1. Create a new file → paste this JSON:

   ```json
   {
      "molecules":{
         "lsInsulin":"malwmrllpllallalwgpdpaaa",
         "bInsulin":"fvnqhlcgshlvealylvcgergffytpkt",
         "aInsulin":"giveqcctsicslyqlenycn",
         "cInsulin":"rreaedlqvgqvelgggpgagslqplalegslqkr"
      },
      "weights":{
         "A":89.09,"C":121.16,"D":133.10,"E":147.13,"F":165.19,
         "G":75.07,"H":155.16,"I":131.17,"K":146.19,"L":131.17,
         "M":149.21,"N":132.12,"P":115.13,"Q":146.15,"R":174.20,
         "S":105.09,"T":119.12,"V":117.15,"W":204.23,"Y":181.19
      },
      "molecularWeightInsulinActual":5807.63
   }
   ```

2. Save as `files/insulin.json`.

---

## 📂 Step 4: Create the JSON File Handler Module

In `jsonFileHandler.py`:

```python
import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
```

This module safely reads a JSON file and returns its contents as a Python dictionary.

---

## ⚙️ Step 5: Create the Main Program

In `calc_weight_json.py`:

```python
import jsonFileHandler

# Read JSON data
data = jsonFileHandler.readJsonFile('files/insulin.json')

if data != "":
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']

    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))

    # Calculating rough molecular weight
    aaWeights = data['weights']
    aaCountInsulin = {x: float(insulin.upper().count(x)) 
                      for x in aaWeights.keys()}
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) 
                      for x in aaWeights.keys()}.values())

    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))
else:
    print("Error. Exiting program")
```

---

## ✅ Expected Output

When you run `calc_weight_json.py`, you should see:

```
bInsulin: fvnqhlcgshlvealylvcgergffytpkt
aInsulin: giveqcctsicslyqlenycn
molecularWeightInsulinActual: 5807.63
The rough molecular weight of insulin: 6696.420000000001
Percent error: 15.30383306099047
```

---

## 🎉 Completion

You have:

* Created and read a JSON file
* Built a reusable file handler module
* Parsed data into Python
* Calculated the rough molecular weight of insulin

This ties together **file handling, modules, JSON, and string/numeric operations** in Python!
