# SQL Basics – Users, Constraints & Multi-Table Queries

This README covers essential SQL concepts used in MySQL, including user management, constraints, keys, and methods for retrieving data from multiple tables.

---

## 📌 Table of Contents

* [How to Create a New MySQL User](#how-to-create-a-new-mysql-user)
* [How to Manage User Privileges](#how-to-manage-user-privileges)
* [Primary Key](#primary-key)
* [Foreign Key](#foreign-key)
* [NOT NULL and UNIQUE Constraints](#not-null-and-unique-constraints)
* [Retrieving Data From Multiple Tables](#retrieving-data-from-multiple-tables)
* [Subqueries](#subqueries)
* [JOIN vs UNION](#join-vs-union)

---

## 🔐 How to Create a New MySQL User

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```

Allow connections from any host:

```sql
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
```

Check existing users:

```sql
SELECT user, host FROM mysql.user;
```

---

## 🛠️ How to Manage User Privileges

### Grant all privileges on a database

```sql
GRANT ALL PRIVILEGES ON db_name.* TO 'username'@'localhost';
```

### Grant specific table privileges

```sql
GRANT SELECT, INSERT, UPDATE ON db_name.table_name TO 'username'@'localhost';
```

### Revoke privileges

```sql
REVOKE ALL PRIVILEGES ON db_name.* FROM 'username'@'localhost';
```

### Apply changes

```sql
FLUSH PRIVILEGES;
```

---

## 🔑 Primary Key

A **PRIMARY KEY**:

* Uniquely identifies each row
* Cannot be `NULL`
* Is indexed automatically

Example:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);
```

---

## 🔗 Foreign Key

A **FOREIGN KEY** links two tables together.

Example:

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

Rules:

* `user_id` must exist in `users.id`
* Enforces relational integrity

---

## ⚙️ NOT NULL and UNIQUE Constraints

### NOT NULL

Value must always be provided.

```sql
name VARCHAR(50) NOT NULL;
```

### UNIQUE

No duplicate values allowed.

```sql
email VARCHAR(100) UNIQUE;
```

Combined:

```sql
email VARCHAR(100) NOT NULL UNIQUE;
```

---

## 📚 Retrieving Data From Multiple Tables

Most commonly done using **JOIN**.

Example:

```sql
SELECT users.name, orders.id
FROM users
JOIN orders ON users.id = orders.user_id;
```

---

## 🔍 Subqueries

A subquery is a query inside another query.

```sql
SELECT name
FROM users
WHERE id = (
    SELECT user_id FROM orders WHERE id = 10
);
```

Subqueries can be used in:

* SELECT
* FROM
* WHERE
* HAVING

---

## 🤝 JOIN vs UNION

### JOIN – combine tables horizontally

```sql
SELECT u.name, o.id
FROM users u
JOIN orders o ON u.id = o.user_id;
```

Types of JOIN:

* `INNER JOIN`
* `LEFT JOIN`
* `RIGHT JOIN`
* `FULL JOIN` (not in MySQL)

### UNION – combine results vertically

```sql
SELECT name FROM users
UNION
SELECT name FROM teachers;
```

Rules:

* Same number of columns
* Compatible data types

---

## ✔️ Done!


