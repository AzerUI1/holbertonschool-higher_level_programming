# 🐍 Python — Complete Beginner to Advanced Guide

<p align="center">  
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" width="200">  
</p>

Python is a **powerful and easy-to-learn** programming language used everywhere:

✅ AI & Machine Learning  
✅ Web Development  
✅ Game Development  
✅ Automation & Scripting  
✅ Data Science  
✅ Robotics & IoT  

---

## 📌 Table of Contents
- ✅ Why Python?
- 🛠 Installing Python
- 🧩 Basic Syntax Examples
- 🔹 Control Flow
- 🎯 Functions
- 📦 Data Structures
- 📚 Modules & Packages
- 📂 File Handling
- 🧱 OOP — Classes & Objects
- ❌ Error Handling
- 🧠 Popular Libraries
- 📘 Learning Resources

---

## 🚀 Why Python?

| Feature | Benefit |
|----------|----------|
| ✅ Simple syntax | Easy for beginners |
| 🧠 Smart | High-level language |
| 🧩 Huge ecosystem | Thousands of libraries |
| 🤖 AI & Data-ready | NumPy, Pandas, PyTorch |
| 🌎 Cross-platform | Works anywhere |

---

## 🛠 Installing Python

🔹 Download from the official website:  
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

Check version:

```bash
python --version
```

Or on Mac/Linux:

```bash
python3 --version
```

---

## 🧩 Basic Syntax Examples

```python
print("Hello Python 👋")

x = 5
y = 3.5
print(x + y)
```

---

## 🔹 Control Flow

```python
age = 16

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Kid")
```

### Loops:

```python
for i in range(5):
    print(i)

while i > 0:
    i -= 1
```

---

## 🎯 Functions

```python
def greet(name):
    print("Hello", name)

greet("Azer")
```

### Lambda (one-line function):

```python
square = lambda x: x * x
```

---

## 📦 Data Structures

```python
# List
fruits = ["apple", "banana"]

# Tuple
point = (4, 5)

# Dictionary
person = {"name": "Azer", "age": 13}

# Set
unique_nums = {1, 2, 3}
```

---

## 📂 File Handling

```python
file = open("data.txt", "r")
print(file.read())
file.close()
```

### Using safe mode:

```python
with open("data.txt") as f:
    print(f.read())
```

---

## 🧱 OOP — Classes & Objects

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(self.brand, "is driving 🚗")

my_car = Car("Tesla")
my_car.drive()
```

---

## ❌ Error Handling

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid number!")
finally:
    print("Done!")
```

---

## 🧠 Popular Python Libraries

| Category | Libraries |
|-----------|------------|
| AI / ML | TensorFlow, PyTorch, Scikit-Learn |
| Data Science | NumPy, Pandas, Matplotlib |
| Web Dev | Django, Flask, FastAPI |
| Games | Pygame |
| Automation | OS, Selenium |
| Networks | Requests, Socket |

### Example:

```python
import random
print(random.randint(1, 10))
```

---

## ✅ Summary Table

| Concept | Purpose |
|----------|----------|
| Variables | Store data |
| Loops | Repeat actions |
| Functions | Reusable code |
| Classes | Build objects |
| Modules | Add features |
| Exceptions | Handle errors |

---

## 📚 Learning Resources

<p align="center">
  <a href="https://docs.python.org/3/">
    <img src="https://img.shields.io/badge/Python%20Docs-Official-blue?style=for-the-badge&logo=python">
  </a>
  <a href="https://www.w3schools.com/python/">
    <img src="https://img.shields.io/badge/W3Schools-Learn-green?style=for-the-badge">
  </a>
  <a href="https://realpython.com/">
    <img src="https://img.shields.io/badge/RealPython-Advanced-purple?style=for-the-badge">
  </a>
</p>

---
