# 🐍 Python File Handling & JSON Guide

This guide covers essential Python topics about **file operations**, **JSON**, and **command-line arguments**.

---

## 🚀 Why Python Programming is Awesome
- Easy to learn and read — clean and simple syntax  
- Powerful — used in AI, web development, automation, and data science  
- Cross-platform — works on Windows, macOS, and Linux  
- Huge community — many free libraries and help online  

---

## 📂 How to Open a File
```python
file = open("example.txt", "r")  # 'r' means read mode
```
**Modes:**
- `"r"` – read
- `"w"` – write (overwrites file)
- `"a"` – append
- `"r+"` – read and write
- `"b"` – binary

---

## ✍️ How to Write Text in a File
```python
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()
```

---

## 📖 How to Read the Full Content of a File
```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

---

## 📃 How to Read a File Line by Line
```python
file = open("example.txt", "r")
for line in file:
    print(line.strip())
file.close()
```

---

## 📍 How to Move the Cursor in a File
```python
file = open("example.txt", "r")
file.seek(5)  # move cursor to position 5
print(file.read())
file.close()
```

---

## ✅ How to Make Sure a File is Closed After Using It
```python
file = open("example.txt", "r")
try:
    print(file.read())
finally:
    file.close()
```

---

## 🔒 What is and How to Use the `with` Statement
Automatically closes the file after use.
```python
with open("example.txt", "r") as file:
    content = file.read()
print(content)
```

---

## 🧩 What is JSON
**JSON (JavaScript Object Notation)** is a lightweight format for storing and exchanging data.
```json
{"name": "Azer", "age": 14}
```

---

## 📦 What is Serialization
Converting a **Python object → JSON string**.

```python
import json
data = {"name": "Azer", "age": 14}
json_str = json.dumps(data)
print(json_str)
```

---

## 🔁 What is Deserialization
Converting a **JSON string → Python object**.

```python
import json
json_str = '{"name": "Azer", "age": 14}'
data = json.loads(json_str)
print(data["name"])
```

---

## 💻 How to Access Command Line Parameters in a Python Script
```python
import sys
print(sys.argv)
```
**Example:**
```bash
python script.py hello world
```
**Output:**
```
['script.py', 'hello', 'world']
```

---

📘 **Author:** Azer Aslanov  
📅 **Updated:** November 2025  
