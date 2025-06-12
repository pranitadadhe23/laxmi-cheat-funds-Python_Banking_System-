import sqlite3

DB_NAME = "bank.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_number INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            balance REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_account_db(name, acc_type, balance):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO accounts (name, type, balance) VALUES (?, ?, ?)", (name, acc_type, balance))
    conn.commit()
    acc_no = cur.lastrowid
    conn.close()
    return acc_no

def get_account_db(acc_no):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts WHERE account_number = ?", (acc_no,))
    account = cur.fetchone()
    conn.close()
    return account

def update_balance_db(acc_no, new_balance):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, acc_no))
    conn.commit()
    conn.close()


    #dbmsS