

✔ `if`
✔ `elif`
✔ `else`
✔ `for` loop
✔ `while` loop
✔ `def` (functions)
✔ `lambda` (anonymous functions)

Includes images, icons, examples, and buttons ✅

---

# 🐍 Python Control Flow + Functions

<p align="center">
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" width="180">
</p>

This guide covers the **most important Python building blocks** that control decisions and repetition in programs! ✅

---

## 🔹 `if`, `elif`, `else` — Decision Making

```python
age = 15

if age >= 18:
    print("✅ Allowed")
elif age >= 10:
    print("🧒 Almost there, but not yet!")
else:
    print("❌ Not allowed!")
```

✔ Python checks conditions **top → down**
✔ Only the **first true** block runs

---

## 🔁 `for` Loop — Repeat Over Items

```python
fruits = ["apple", "banana", "cherry"]

for item in fruits:
    print("🍓 I like", item)
```

✔ Best for repeating a known number of times
✔ Works with lists, strings, numbers, etc.

---

### `range()` with `for`

```python
for i in range(1, 6):
    print(i)
```

➡ Prints numbers **1 to 5**

---

## 🔄 `while` Loop — Repeat Until False

```python
count = 3

while count > 0:
    print(count)
    count -= 1

print("🚀 Go!")
```

⚠ Must update condition → to prevent infinite loop!

---

## 🎯 Functions — `def`

Functions = reusable blocks of code ✅

```python
def greet(name):
    print("Hello", name, "👋")

greet("Azer")
```

| Benefit     | Why it matters    |
| ----------- | ----------------- |
| ✅ Reusable  | No repeating code |
| ✅ Organized | Easier to read    |
| ✅ Scalable  | Larger projects   |

---

## ⚡ Lambda Functions (Anonymous)

Short, one-line functions ✅

```python
square = lambda x: x * x
print(square(6))  # 36
```

✔ Often used for **sorting** or **data filters**

Another example:

```python
add = lambda a, b: a + b
print(add(3, 7))  # 10
```

---

## ✅ All Concepts Summary Table

| Feature         | Keyword  | Usage                  |
| --------------- | -------- | ---------------------- |
| Condition       | `if`     | Check a condition      |
| More conditions | `elif`   | Extra tests            |
| Fallback        | `else`   | Runs if all failed     |
| Loop            | `for`    | Repeat through items   |
| Loop            | `while`  | Repeat until false     |
| Function        | `def`    | Define reusable code   |
| Small function  | `lambda` | Quick inline functions |

---

## 📌 Mini Practice Program

```python
def multiply_or_square(n):
    if n > 10:
        return n * n
    else:
        return n * 2

for x in [5, 12, 3]:
    print(multiply_or_square(x))
```

---

## 📚 Learn More

<p align="center">
<a href="https://docs.python.org/3/tutorial/controlflow.html">
  <img src="https://img.shields.io/badge/Python_Docs-Control_Flow-blue?style=for-the-badge&logo=python">
</a>
<a href="https://www.w3schools.com/python/python_conditions.asp">
  <img src="https://img.shields.io/badge/W3Schools-Conditions-green?style=for-the-badge">
</a>
<a href="https://realpython.com/python-functions/">
  <img src="https://img.shields.io/badge/RealPython-Functions-purple?style=for-the-badge">
</a>
</p>

---
