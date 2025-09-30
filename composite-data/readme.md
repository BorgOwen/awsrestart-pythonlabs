# Working with Composite Data Types

## Lab Overview

A **composite data type** is any data type that is made up of primitive data types.
Think of it like a **turducken**: a chicken stuffed into a duck, stuffed into a turkey.
In this lab, you will create a data type that consists of a string inside a dictionary, which is then stored in a list.

### What you will learn

* Use numeric data types
* Use string data types
* Use the dictionary data type
* Use the list data type
* Use a for loop
* Use the `print()` function
* Use the `if` statement
* Use the `else` statement
* Use the `import` statement

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
* Save it as `composite-data.py` in `/home/ec2-user/environment`.

---

### 2. Open the Terminal

* Open a new terminal in Cloud9.
* Confirm you’re in `/home/ec2-user/environment` with:

  ```bash
  pwd
  ```

---

### 3. Create Car Inventory Data

#### Create a CSV File

* From the menu bar, choose **File > New File**.
* Save it as `car_fleet.csv`.
* Copy and paste the following into the file:

```csv
vin,make,model,year,range,topSpeed,zeroSixty,mileage
TMX20122,AnyCompany Motors,Coupe,2012,335,155,4.1,50000
TM320163,AnyCompany Motors,Sedan,2016,240,140,5.2,20000
TMX20121,AnyCompany Motors,SUV,2012,295,155,4.7,100000
TMX20204,AnyCompany Motors,Truck,2020,300,155,3.5,0
```

---

### 4. Create a Car Inventory Program

#### Import Required Modules

```python
import csv
import copy
```

#### Define a Dictionary Template

```python
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}
```

#### Print Keys and Values

```python
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))
```

#### Define an Empty Inventory List

```python
myInventoryList = []
```

---

### 5. Copy CSV Data into Memory

```python
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.')
```

**Note:**

* `copy.deepcopy()` ensures that a fresh copy of the dictionary is created for each vehicle.
* Without it, only the last entry would remain in memory.

---

### 6. Print the Car Inventory

```python
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")
```

---

## End of Lab

Congratulations! You have worked with **composite data types** in Python by combining dictionaries, lists, and CSV data.

