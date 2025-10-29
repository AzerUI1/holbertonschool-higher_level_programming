
---

# 🐍 Python Error Handling — `try` / `except`

<p align="center">
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" width="200">
</p>

---

## 🔹 What is Exception Handling?

> Prevent your program from **crashing** when something unexpected happens.

---

### 🚀 Quick Navigation

<p align="center">
<a href="#-basic-example">
  <img src="https://img.shields.io/badge/Basic-Examples-blue?style=for-the-badge">
</a>
<a href="#-catching-specific-errors">
  <img src="https://img.shields.io/badge/Specific-Errors-purple?style=for-the-badge">
</a>
<a href="#-custom-exceptions">
  <img src="https://img.shields.io/badge/Custom-Exceptions-red?style=for-the-badge">
</a>
<a href="#-best-practices">
  <img src="https://img.shields.io/badge/Best-Practices-green?style=for-the-badge">
</a>
</p>

---

## ✅ Basic Example

```python
try:
    num = int(input("Enter a number: "))
    print("✅ Result:", num * 5)
except:
    print("❌ Invalid input! Please enter a number.")
```

---

## 🎯 Catching Specific Errors

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("🚫 Division by zero is not allowed!")
```

---

### 🔍 Common Exceptions

| Icon | Exception           | When it Happens         |
| ---- | ------------------- | ----------------------- |
| ❌    | `ZeroDivisionError` | Divide by 0             |
| 🔢   | `ValueError`        | Wrong value format      |
| 📦   | `KeyError`          | Missing dictionary key  |
| 📏   | `IndexError`        | Invalid list index      |
| ⚙️   | `TypeError`         | Wrong type in operation |
| 📂   | `FileNotFoundError` | Missing file            |

---

## ➕ `else` & `finally`

```python
try:
    file = open("log.txt")
except FileNotFoundError:
    print("📂 File missing!")
else:
    print("✅ File opened")
finally:
    print("🔒 Always runs!")
```

---

## 🧱 Multiple Exceptions

```python
try:
    x = int("abc")
except ValueError:
    print("📛 That's not a number!")
except Exception as e:
    print("⚡ Unexpected error:", e)
```

---

## 💥 Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")

try:
    check_age(-5)
except InvalidAgeError as e:
    print("❌ Error:", e)
```

<p align="center">
  <img src="https://media.giphy.com/media/26FLdmIp6wJr91JAI/giphy.gif" width="250">
</p>

---

## 🧠 Best Practices

✅ Catch **specific** exceptions
✅ Keep try-blocks **short**
✅ Log errors for debugging
✅ Clean up with `finally`

---

## 📚 Useful Buttons

<p align="center">
<a href="https://docs.python.org/3/tutorial/errors.html">
  <img src="https://img.shields.io/badge/Python%20Docs-Exceptions-blue?style=for-the-badge&logo=python">
</a>
<a href="https://realpython.com/python-exceptions/">
  <img src="https://img.shields.io/badge/Real%20Python-Guide-success?style=for-the-badge">
</a>
</p>

---

## ✅ Summary Table

| Keyword   | Action             |
| --------- | ------------------ |
| `try`     | Test risky code    |
| `except`  | Handle the error   |
| `else`    | Runs if no error   |
| `finally` | Runs always        |
| `raise`   | Throw custom error |

---




