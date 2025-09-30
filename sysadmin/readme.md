# 🖥️ Introducing System Administration with Python

## Lab Overview

Linux allows you to perform many administrative tasks from the **Bash command line**. Python provides modules like **os** and **subprocess** that let you run those same commands directly from Python.

In this lab, you will:

* Use `os.system()` to run a Bash command
* Use `subprocess.run()` to run Bash commands

**Estimated completion time:** 30 minutes

---

## 🔑 Step 1: Accessing the AWS Cloud9 IDE

1. Start the lab by choosing **Start Lab**.
2. Wait for **Lab status: ready**, then close the panel.
3. Choose **AWS** at the top of the instructions.
4. The AWS Management Console opens in a new tab (auto login).

⚠️ If it doesn’t open, allow pop-ups in your browser.

5. In the AWS console, go to **Services > Cloud9**.
6. Find the `reStart-python-cloud9` environment and choose **Open IDE**.

---

## 📂 Step 2: Creating Your Python File

1. In the menu bar, choose **File > New From Template > Python File**.
2. Delete the sample code.
3. Save the file as `sys-admin.py` under `/home/ec2-user/environment`.

---

## 💻 Step 3: Accessing the Terminal

1. In Cloud9, choose **+ → New Terminal**.
2. Verify your directory:

```bash
pwd
```

Expected output:

```
/home/ec2-user/environment
```

---

## 🧩 Exercise 1: Using os.system()

Run a Bash command from Python with the `os` module:

```python
import os
os.system("ls")
```

✅ Output: Shows the files in your directory (e.g., `sys-admin.py README.md`).

---

## 🧩 Exercise 2: Using subprocess.run()

The `subprocess` module is more powerful than `os.system()`.

```python
import subprocess
subprocess.run(["ls"])
```

✅ Output: Lists directory contents.

---

## 🧩 Exercise 3: Adding an Argument

Use `-l` to display details in long format:

```python
subprocess.run(["ls", "-l"])
```

✅ Output:

```
-rw-r--r-- 1 ec2-user ec2-user   55 sys-admin.py
-rw-r--r-- 1 ec2-user ec2-user  343 sys-admin_2.py
-rw-r--r-- 1 ec2-user ec2-user  569 README.md
```

---

## 🧩 Exercise 4: Adding a File Argument

Specify a single file:

```python
subprocess.run(["ls", "-l", "README.md"])
```

✅ Output: Detailed info about `README.md` only.

---

## 🧩 Exercise 5: Retrieving System Info

Run the `uname -a` command:

```python
command = "uname"
commandArgument = "-a"
print(f"Gathering system information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])
```

✅ Output: Linux system details.

---

## 🧩 Exercise 6: Retrieving Active Processes

Run the `ps -x` command:

```python
command = "ps"
commandArgument = "-x"
print(f"Gathering active process information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])
```

✅ Output: Active process list.

---

## 🎉 Completion

You have successfully:

* Run Bash commands with Python’s `os` module
* Used the more advanced `subprocess.run()` to execute commands with arguments
* Retrieved system and process information

Congratulations — you just did system administration with Python!
