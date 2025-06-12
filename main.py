from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QInputDialog, QMessageBox, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Banking.database import init_db, create_account_db, get_account_db, update_balance_db

class BankApp(QWidget):
    def __init__(self):
        super().__init__()

        init_db()  # Initialize DB table
        self.user = None

        self.setWindowTitle("Laxmi Cheat Funds")
        self.setGeometry(100, 100, 450, 400)

        self.setStyleSheet("""
            QWidget {
                background-color: #f9f9f9;
                font-family: Arial;
            }
            QPushButton {
                background-color: #6200EE;
                color: white;
                padding: 10px;
                border-radius: 8px;
                font-size: 14px;
                width: 200px;
            }
            QPushButton:hover {
                background-color: #3700B3;
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #333;
            }
        """)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(15)
        self.layout.setAlignment(Qt.AlignCenter)

        self.init_homepage()

        self.setLayout(self.layout)

    def init_homepage(self):
        self.clear_layout()

        self.title = QLabel("🏦 Welcome to Laxmi Cheat Funds")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Arial", 16, QFont.Bold))
        self.layout.addWidget(self.title)

        self.create_btn = QPushButton("➕ Create Account")
        self.create_btn.clicked.connect(self.create_account)
        self.layout.addWidget(self.create_btn, alignment=Qt.AlignCenter)

        self.login_btn = QPushButton("🔐 Login")
        self.login_btn.clicked.connect(self.login)
        self.layout.addWidget(self.login_btn, alignment=Qt.AlignCenter)

        self.exit_btn = QPushButton("❌ Exit")
        self.exit_btn.clicked.connect(self.close)
        self.layout.addWidget(self.exit_btn, alignment=Qt.AlignCenter)

    def create_account(self):
        name, ok = QInputDialog.getText(self, "Create Account", "Enter your name:")
        if not ok or not name:
            return

        acc_type, ok = QInputDialog.getText(self, "Account Type", "Enter type (savings/current):")
        if not ok:
            return

        amount, ok = QInputDialog.getDouble(self, "Deposit", "Initial deposit:")
        if not ok:
            return

        acc_no = create_account_db(name, acc_type.lower(), amount)
        QMessageBox.information(self, "Success", f"Account created!\nAccount Number: {acc_no}")

    def login(self):
        acc_no, ok = QInputDialog.getInt(self, "Login", "Enter account number:")
        if not ok:
            return

        account = get_account_db(acc_no)
        if account:
            self.user = {
                "account_number": account[0],
                "name": account[1],
                "type": account[2],
                "balance": account[3]
            }
            self.show_dashboard()
        else:
            QMessageBox.warning(self, "Error", "Account not found.")

    def show_dashboard(self):
        self.clear_layout()

        welcome = QLabel(f"👤 Hello, {self.user['name']} (Acc No: {self.user['account_number']})")
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(welcome)

        self.layout.addWidget(self.create_button("💰 Check Balance", self.check_balance))
        self.layout.addWidget(self.create_button("📥 Deposit", self.deposit_money))
        self.layout.addWidget(self.create_button("📤 Withdraw", self.withdraw_money))

        if self.user['type'] == 'savings':
            self.layout.addWidget(self.create_button("📈 Add Interest", self.add_interest))

        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.create_button("🔓 Logout", self.logout), alignment=Qt.AlignCenter)

    def create_button(self, label, func):
        btn = QPushButton(label)
        btn.clicked.connect(func)
        btn.setFixedWidth(200)
        return btn

    def check_balance(self):
        QMessageBox.information(self, "Balance", f"₹{self.user['balance']:.2f}")

    def deposit_money(self):
        amount, ok = QInputDialog.getDouble(self, "Deposit", "Amount:")
        if ok:
            self.user['balance'] += amount
            update_balance_db(self.user['account_number'], self.user['balance'])
            QMessageBox.information(self, "Success", f"Deposited ₹{amount:.2f}")

    def withdraw_money(self):
        amount, ok = QInputDialog.getDouble(self, "Withdraw", "Amount:")
        if ok:
            if self.user['balance'] >= amount:
                self.user['balance'] -= amount
                update_balance_db(self.user['account_number'], self.user['balance'])
                QMessageBox.information(self, "Success", f"Withdrew ₹{amount:.2f}")
            else:
                QMessageBox.warning(self, "Error", "Insufficient balance.")

    def add_interest(self):
        months, ok = QInputDialog.getInt(self, "Interest", "Enter number of months:")
        if ok:
            rate = 0.04  # 4% yearly interest
            interest = rate * months * self.user['balance']
            self.user['balance'] += interest
            update_balance_db(self.user['account_number'], self.user['balance'])
            QMessageBox.information(self, "Interest Added", f"₹{interest:.2f} credited.")

    def logout(self):
        self.user = None
        self.init_homepage()

    def clear_layout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

# Run app
if __name__ == '__main__':
    app = QApplication([])
    window = BankApp()
    window.show()
    app.exec_()
