# python-object_relational_mapping
---

## Overview

Quick, hands-on examples showing:

* a minimal `DB` wrapper using `sqlite3`,
* model definitions with an ORM-like layer (`Model` base class),
* simple CRUD operations,
* migration-ish helper,
* example scripts to create and query records,
* a small `web_demo` folder with SVG icons and button examples (HTML + CSS) to use as repo assets.

---

## Example of Files

* `README.md` (this file)
* `requirements.txt`
* `src/db.py` — database connection and helper
* `src/model.py` — lightweight ORM base and example `User` model
* `src/crud.py` — CRUD example functions
* `examples/create_and_query.py` — runnable example
* `web_demo/index.html` — small demo page with icons, buttons and images
* `web_demo/styles.css` — styles for demo
* `assets/icons/database.svg` — database icon (SVG)
* `assets/icons/user.svg` — user icon (SVG)
* `assets/buttons/primary.svg` — button-like SVG
* `assets/images/sample.png` — placeholder image (create or replace)

---

## requirements.txt

```
# Keep dependencies minimal; no full SQLAlchemy to show core concepts
# (optional) You can pip install these if you want helper libs
```

---

## src/db.py

```python
# src/db.py
# Minimal sqlite3 wrapper
import sqlite3
from typing import Optional

class DB:
    def __init__(self, path: str = 'data.db'):
        self.path = path
        self.conn: Optional[sqlite3.Connection] = None

    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.path)
            self.conn.row_factory = sqlite3.Row
        return self.conn

    def execute(self, sql: str, params: tuple = ()):  # execute a statement
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        return cur

    def query(self, sql: str, params: tuple = ()):  # fetch multiple rows
        cur = self.execute(sql, params)
        return cur.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
```

---

## src/model.py

```python
# src/model.py
# Very small ORM-like base using sqlite3
from typing import Any, Dict, List, Tuple
from src.db import DB

db = DB()

class Field:
    def __init__(self, column_type: str, pk: bool=False):
        self.column_type = column_type
        self.pk = pk

class ModelMeta(type):
    def __new__(mcs, name, bases, namespace):
        fields = {}
        for key, val in list(namespace.items()):
            if isinstance(val, Field):
                fields[key] = val
                namespace.pop(key)
        namespace['_fields'] = fields
        return super().__new__(mcs, name, bases, namespace)

class Model(metaclass=ModelMeta):
    table_name: str = ''

    @classmethod
    def create_table(cls):
        cols = []
        for name, field in cls._fields.items():
            col = f"{name} {field.column_type}"
            if field.pk:
                col += " PRIMARY KEY"
            cols.append(col)
        sql = f"CREATE TABLE IF NOT EXISTS {cls.table_name} ({', '.join(cols)})"
        db.execute(sql)

    def __init__(self, **kwargs):
        for f in self._fields:
            setattr(self, f, kwargs.get(f))

    def save(self):
        keys = [k for k in self._fields if not self._fields[k].pk]
        vals = [getattr(self, k) for k in keys]
        placeholders = ','.join(['?']*len(vals))
        sql = f"INSERT INTO {self.table_name} ({', '.join(keys)}) VALUES ({placeholders})"
        db.execute(sql, tuple(vals))

    @classmethod
    def all(cls) -> List[Dict[str, Any]]:
        rows = db.query(f"SELECT * FROM {cls.table_name}")
        return [dict(r) for r in rows]

    @classmethod
    def filter(cls, where: str, params: Tuple=()) -> List[Dict[str, Any]]:
        rows = db.query(f"SELECT * FROM {cls.table_name} WHERE {where}", params)
        return [dict(r) for r in rows]
```

---

## src/crud.py

```python
# src/crud.py
from src.model import Model, Field, db

class User(Model):
    table_name = 'users'
    id = Field('INTEGER', pk=True)
    name = Field('TEXT')
    email = Field('TEXT')

# helper functions

def init():
    db.connect()
    User.create_table()

def create_user(name: str, email: str):
    u = User(name=name, email=email)
    u.save()
    return u

def list_users():
    return User.all()

def find_by_email(email: str):
    return User.filter('email = ?', (email,))
```

---

## examples/create_and_query.py

```python
# examples/create_and_query.py
from src.crud import init, create_user, list_users, find_by_email

if __name__ == '__main__':
    init()  # create DB and tables
    create_user('Alice', 'alice@example.com')
    create_user('Bob', 'bob@example.com')
    print('All users:')
    print(list_users())
    print('Find Bob:')
    print(find_by_email('bob@example.com'))
```

---

## web_demo/index.html

```html
<!-- web_demo/index.html -->
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>ORM Demo — Icons & Buttons</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <header class="top">
      <img class="icon" src="../assets/icons/database.svg" alt="DB icon" />
      <h1>Python ORM — Demo</h1>
    </header>

    <section class="cards">
      <div class="card">
        <img class="icon-small" src="../assets/icons/user.svg" alt="user" />
        <h2>Users</h2>
        <button class="btn primary">Create user</button>
        <button class="btn ghost">List users</button>
      </div>

      <div class="card">
        <img class="sample" src="../assets/images/sample.png" alt="sample" />
        <h2>Sample image</h2>
        <svg class="btn-svg" viewBox="0 0 200 60" xmlns="http://www.w3.org/2000/svg">
          <rect x="0" y="0" width="200" height="60" rx="8" />
          <text x="100" y="36" dominant-baseline="middle" text-anchor="middle">SVG Button</text>
        </svg>
      </div>
    </section>

  </body>
</html>
```

---

## web_demo/styles.css

```css
/* web_demo/styles.css */
body { font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; padding: 24px; }
.top { display:flex; align-items:center; gap:12px }
.icon { width:48px; height:48px }
.cards { display:flex; gap:18px; margin-top:20px }
.card { border:1px solid #ddd; padding:12px; border-radius:8px; width:220px }
.btn { padding:8px 12px; border-radius:6px; cursor:pointer; margin-top:8px }
.btn.primary { background: #1d4ed8; color:#fff; border:none }
.btn.ghost { background:transparent; border:1px solid #888 }
.icon-small { width:28px }
.sample { width:100%; height:auto; margin-top:8px }
.btn-svg { width:200px; height:60px; margin-top:8px }
```

---

## assets/icons/database.svg

```svg
<!-- assets/icons/database.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" aria-hidden="true">
  <ellipse cx="32" cy="14" rx="20" ry="6" fill="none" stroke="#111" stroke-width="2"/>
  <path d="M12 14v12c0 3.3 8.9 6 20 6s20-2.7 20-6V14" fill="none" stroke="#111" stroke-width="2"/>
  <path d="M12 26v12c0 3.3 8.9 6 20 6s20-2.7 20-6V26" fill="none" stroke="#111" stroke-width="2"/>
</svg>
```

---

## assets/icons/user.svg

```svg
<!-- assets/icons/user.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <circle cx="32" cy="20" r="10" fill="none" stroke="#111" stroke-width="2" />
  <path d="M12 52c0-11 8.5-20 20-20s20 9 20 20" fill="none" stroke="#111" stroke-width="2" />
</svg>
```

---

## assets/buttons/primary.svg

```svg
<!-- assets/buttons/primary.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 40" width="140" height="40">
  <rect rx="8" width="140" height="40" fill="#2563eb" />
  <text x="70" y="26" font-family="sans-serif" font-size="14" fill="#fff" text-anchor="middle">Primary</text>
</svg>
```

---

## assets/images/sample.png

A placeholder PNG image. You can replace this with a real screenshot or image file. (Tip: use a 800×450 PNG for good results.)

---

## How to use

1. Create the repository locally:

```bash
mkdir python-object_relational_mapping
cd python-object_relational_mapping
# create folders and files as in this draft
```

2. Run the example:

```bash
python -m examples.create_and_query
```

3. Open `web_demo/index.html` in your browser to preview the icons and buttons.

---
