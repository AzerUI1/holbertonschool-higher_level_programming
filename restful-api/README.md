
<h1 align="center">🌐 RESTful API — Complete Guide</h1>

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/3408/3408597.png" width="150">
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Language-Python-blue?logo=python"></a>
  <a href="#"><img src="https://img.shields.io/badge/Framework-Flask-orange?logo=flask"></a>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-green"></a>
</p>

---

## 🚀 Overview

A **RESTful API (Representational State Transfer)** is an **architecture style** used to design web services that communicate over **HTTP**. It defines a set of rules developers follow when creating APIs, ensuring they are simple, scalable, and reusable.

---

## 🧩 Core Principles of REST

| Principle | Description |
|------------|-------------|
| **Statelessness** | Each request from the client must contain all necessary information. No session is stored on the server. |
| **Client-Server** | The client and the server are independent — they communicate only through requests and responses. |
| **Cacheable** | Responses should define whether they can be cached to improve performance. |
| **Uniform Interface** | Consistent resource representation through endpoints (URLs). |
| **Layered System** | APIs can have multiple layers (proxy, load balancer) without affecting client requests. |

---

## ⚙️ HTTP Methods

| Method | Description |
|--------|--------------|
| `GET` | Retrieve data |
| `POST` | Create data |
| `PUT` | Update data |
| `DELETE` | Remove data |

---

## 💡 Example: Simple Flask RESTful API

```python
# Importing Flask
from flask import Flask, jsonify, request

# Creating the app
app = Flask(__name__)

# Fake database
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# GET: Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)  # Return all users in JSON format

# GET: Retrieve a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user) if user else ("User not found", 404)

# POST: Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()  # Get data from request
    users.append(new_user)         # Add to fake DB
    return jsonify(new_user), 201  # Return created user with status 201

# PUT: Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify(user)
    return ("User not found", 404)

# DELETE: Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return ("", 204)  # No content

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🧠 Explanation (Line-by-Line)

| Line | Explanation |
|------|--------------|
| `from flask import Flask, jsonify, request` | Import Flask framework and helpers for JSON and HTTP requests. |
| `app = Flask(__name__)` | Initialize the Flask application. |
| `users = [...]` | A fake database list of users. |
| `@app.route('/users', methods=['GET'])` | Define endpoint to get all users. |
| `return jsonify(users)` | Converts Python data to JSON. |
| `request.get_json()` | Extracts JSON data from the client’s request. |
| `app.run(debug=True)` | Runs the Flask development server. |

---

## 🧰 Tools Used

- 🐍 **Python 3**
- ⚡ **Flask**
- 🔐 **Postman** (for API testing)
- 🧩 **cURL** (for command-line requests)

---

## 📸 Demo Screenshot
<p align="center">
  <img src="https://i.imgur.com/H9D7NvT.png" width="600">
</p>

---

## 📥 Installation

```bash
git clone https://github.com/yourusername/restful-api-guide.git
cd restful-api-guide
pip install flask
python app.py
```

---

## 🧾 License
This project is licensed under the MIT License.

---

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Download-README-blue?style=for-the-badge&logo=github"></a>
</p>
