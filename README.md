# 🏦 Laxmi Cheat Funds – Banking Management System

A simple GUI-based banking application developed in **Python** using **PyQt5** with **SQLite** integration for data persistence.
This application allows users to create savings or current accounts, log in, deposit or withdraw money, and calculate interest (for savings).

---

## 📁 Project Structure

📂 banking  
├── init.py # Package initializer  
├── account.py # Contains SavingAccount and CurrentAccount classes  
├── transaction.py # Handles deposit and withdraw functions  
├── database.py # Database logic (account table creation, insert, fetch)  
📄 main.py # Main PyQt5 GUI application  
📄 bank.db # SQLite database storing account data  
📄 README.md # Project documentation  


## 🚀 Features

- Create Savings or Current account
- Auto-generated Account Numbers (starting from 1000)
- Deposit and Withdraw Money
- Add Interest (for savings accounts)
- Login and Logout functionality
- Data stored in `bank.db` (SQLite)
- Styled and responsive PyQt5 UI

---

## 🛠️ Tech Stack

- **Python 3**
- **PyQt5** (for GUI)
- **SQLite** (for persistent backend storage)
- **VS Code / DB Browser for SQLite** (optional, for viewing data)

---

## ▶️ How to Run

### 1. 📦 Install Dependencies

```bash
pip install pyqt5
```
2. 🏁 Run the Application
Make sure you’re in the project folder and run:
```bash
python main.py
```

💾 Database
The database is stored in bank.db

Uses SQLite and is created automatically if not found

You can browse the data using:

DB Browser for SQLite

Or SQLite extension in VS Code:

Install SQLite extension by alexcvzz

Open bank.db in VS Code

Use the SQL Explorer to view tables and data

📊 Tables & Data Schema
The application stores account data in the accounts table:

Column Name	Type	Description
id	INTEGER	Auto-increment primary key
name	TEXT	Account holder name
balance	REAL	Account balance
acc_type	TEXT	Account type: 'savings' or 'current'
account_number	INTEGER	Unique account number starting at 1000

📌 Example Use
Launch the app

Create an account by entering your name, type, and initial deposit

Login using the generated account number

Access the dashboard to:

Check balance

Deposit / Withdraw

Add interest (if savings)

Logout

✨ Screenshots
(You can add screenshots here)

📬 Contact
For queries or collaboration:
Pranita Dadhe – LinkedIn | GitHub

📄 License
This project is licensed under the MIT License.

---

Let me know if you'd like help with:
- Adding a `.gitignore`
- Uploading the project to GitHub
- Adding real screenshots
- Writing a `LICENSE` file

I'll help you set it all up properly!







