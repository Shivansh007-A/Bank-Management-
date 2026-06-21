# Bank Management System

## Overview

A simple Bank Management System developed using Python and MySQL for managing customer accounts and basic banking transactions. The application provides a menu-driven interface that allows users to create accounts, deposit money, withdraw money, and view account records.

## Features

* Create new customer accounts
* Deposit money into existing accounts
* Withdraw money from accounts
* Display customer account details
* Store and manage data using MySQL
* Real-time balance updates

## Technologies Used

* Python
* MySQL
* MySQL Connector

## Database Structure

### Table: records

| Column | Description     |
| ------ | --------------- |
| id     | Customer ID     |
| Name   | Customer Name   |
| acc_no | Account Number  |
| amount | Account Balance |

## Project Workflow

1. Connect to MySQL database.
2. Display menu options.
3. Perform banking operations:

   * View records
   * Deposit money
   * Withdraw money
   * Create new account
4. Update database records accordingly.
5. Commit changes to maintain data consistency.

## Key Learning Outcomes

* Python and MySQL integration
* SQL query execution
* CRUD operations
* Database management
* Transaction handling
* Menu-driven application development

## How to Run

### Install Dependency

```bash
pip install mysql-connector-python
```

### Create Database

```sql
CREATE DATABASE abc;
```

### Create Table

```sql
CREATE TABLE records(
    id INT PRIMARY KEY,
    Name VARCHAR(100),
    acc_no BIGINT,
    amount FLOAT
);
```

### Run the Program

```bash
python bank_management.py
```

## Future Improvements

* User authentication system
* Transaction history tracking
* GUI-based interface
* Secure password encryption
* Account search functionality

## Author

**Shivansh**

## Source Code
<a href="https://github.com/Shivansh007-A/Bank-Management-/blob/main/Bank_Management_sql.py">
View Source Code
</a>
