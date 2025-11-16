---

# SQL Scripting README

### Working With Databases Beyond Queries

This document provides an overview of **SQL scripting** for managing databases, automating workflows, and handling operational tasks *without focusing on data-retrieval queries*. SQL scripting typically consists of a sequence of SQL commands combined into a file (e.g., `.sql`) that can be executed as a batch or scheduled process.

---

## 📚 What Is SQL Scripting?

SQL scripting involves writing and executing **multi-statement SQL files** to automate or standardize database operations.
Instead of running commands one by one, scripting allows you to:

* Set up database structures
* Apply updates or patches
* Manage users and permissions
* Automate backups or maintenance tasks
* Run administrative procedures

SQL scripts are especially useful in production environments, CI/CD pipelines, backups, and repeatable deployments.

---

## 🏗️ Database Creation & Setup Scripts

### Creating a Database

```sql
CREATE DATABASE app_data;
```

### Selecting a Database

```sql
USE app_data;
```

### Creating Tables and Structures

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Running Multiple Commands in Setup Scripts

Scripts often combine many statements:

```sql
-- setup.sql
CREATE DATABASE app_data;
USE app_data;

CREATE TABLE logs (...);
CREATE TABLE settings (...);

CREATE INDEX idx_logs_timestamp ON logs(timestamp);
```

Running this file builds your entire environment in one step.

---

## 🔧 Schema Management (Migrations)

SQL scripts are widely used for schema versioning and updates:

### Adding Columns

```sql
ALTER TABLE users
ADD COLUMN last_login TIMESTAMP NULL;
```

### Modifying Existing Columns

```sql
ALTER TABLE users
MODIFY COLUMN username VARCHAR(150);
```

### Dropping / Renaming Columns

```sql
ALTER TABLE users DROP COLUMN last_login;
ALTER TABLE users RENAME COLUMN password_hash TO pwd_hash;
```

### Versioned Migration Example

```
migrations/
 ├── 001_init.sql
 ├── 002_add_user_metadata.sql
 └── 003_create_audit_system.sql
```

Migrations help keep database structure consistent across environments.

---

## 🔐 User Management & Permissions

SQL scripts can also configure access control.

### Creating Users

```sql
CREATE USER 'app_user' IDENTIFIED BY 'securePass123';
```

### Granting Permissions

```sql
GRANT SELECT, INSERT, UPDATE, DELETE
ON app_data.*
TO 'app_user';
```

### Revoking Permissions

```sql
REVOKE DELETE ON app_data.* FROM 'app_user';
```

These scripts are often used during deployment or onboarding.

---

## 🛠️ Stored Procedures, Functions & Automation

Stored routines can be managed via SQL scripts as well.

### Creating a Stored Procedure

```sql
DELIMITER $$

CREATE PROCEDURE cleanup_old_logs()
BEGIN
    DELETE FROM logs WHERE timestamp < NOW() - INTERVAL 30 DAY;
END $$

DELIMITER ;
```

### Running the Procedure in a Script

```sql
CALL cleanup_old_logs();
```

Stored procedures are often included in maintenance scripts.

---

## 🗂️ Backup & Restore Scripts

### Backing Up (Vendor-Specific Examples)

**MySQL**

```bash
mysqldump app_data > backup.sql
```

**PostgreSQL**

```bash
pg_dump app_data > backup.sql
```

### Restoring

```bash
psql app_data < backup.sql
```

You may wrap these in shell scripts or scheduled tasks (cron, Windows Task Scheduler).

---

## 🚀 Deployment Scripts (CI/CD)

Common uses in automated environments:

* Create databases if not exist
* Apply migrations
* Initialize system data
* Set or update roles
* Run maintenance routines

Example outline:

```sql
-- deployment.sql
SOURCE migrations/001_init.sql;
SOURCE migrations/002_add_indexes.sql;
SOURCE routines/cleanup_old_logs.sql;
```

---

## 📄 Best Practices

* Keep scripts **idempotent** (safe to run more than once).
* Add descriptive **comments** at the top of each script.
* Use **version control** to track schema changes.
* Test scripts in staging before production.
* Avoid embedding confidential data (passwords, secrets).
* Use transaction blocks when possible.

```sql
START TRANSACTION;

-- many operations

COMMIT;
```

---

## ✔️ Summary

SQL scripting goes far beyond running queries. It provides a powerful way to:

* Build and manage database structures
* Control access and permissions
* Automate updates and maintenance
* Standardize deployments
* Manage stored routines and backups

With well-designed SQL scripts, database operations become predictable, repeatable, and easy to automate.

---
