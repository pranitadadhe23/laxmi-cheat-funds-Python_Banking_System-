from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QInputDialog, QMessageBox, QSpacerItem, QSizePolicy, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Banking.account import SavingAccount, CurrentAccount
from Banking.transaction import deposit, withdraw

# Dictionary to store all created accounts
accounts = {}

class BankApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Laxmi Cheat Funds")
        self.setGeometry(100, 100, 450, 400)

        self.user = None  # Currently logged-in user

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
        self.layout.setAlignment(Qt.AlignTop)

        self.title = QLabel("🏦 Welcome to Laxmi Cheat Funds")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Arial", 16, QFont.Bold))
        self.layout.addWidget(self.title)

        # Initial Home Screen Buttons
        self.create_btn = QPushButton("➕ Create Account")
        self.create_btn.clicked.connect(self.create_account)
        self.layout.addWidget(self.wrap_button(self.create_btn))

        self.login_btn = QPushButton("🔐 Login")
        self.login_btn.clicked.connect(self.login)
        self.layout.addWidget(self.wrap_button(self.login_btn))

        self.exit_btn = QPushButton("❌ Exit")
        self.exit_btn.clicked.connect(self.close)
        self.layout.addWidget(self.wrap_button(self.exit_btn))

        self.setLayout(self.layout)

    # Wrap a button in a horizontal layout to center it
    def wrap_button(self, btn):
        btn.setFixedWidth(200)
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(btn)
        h_layout.addStretch()
        container = QWidget()
        container.setLayout(h_layout)
        return container

    # Create centered button dynamically with event
    def create_button(self, label, func):
        btn = QPushButton(label)
        btn.clicked.connect(func)
        return self.wrap_button(btn)

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

        if acc_type.lower() == 'savings':
            acc = SavingAccount(name, amount)
        elif acc_type.lower() == 'current':
            acc = CurrentAccount(name, amount)
        else:
            QMessageBox.warning(self, "Error", "Invalid account type.")
            return

        accounts[acc.account_number] = acc
        QMessageBox.information(self, "Success", f"Account created! Number: {acc.account_number}")

    def login(self):
        acc_no, ok = QInputDialog.getInt(self, "Login", "Enter account number:")
        if not ok:
            return

        if acc_no in accounts:
            self.user = accounts[acc_no]
            self.show_dashboard()
        else:
            QMessageBox.warning(self, "Error", "Account not found.")

    def show_dashboard(self):
        self.clear_layout()

        welcome = QLabel(f"👤 Hello, {self.user.name} (Acc No: {self.user.account_number})")
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(welcome)

        self.layout.addWidget(self.create_button("💰 Check Balance", self.check_balance))
        self.layout.addWidget(self.create_button("📥 Deposit", self.deposit_money))
        self.layout.addWidget(self.create_button("📤 Withdraw", self.withdraw_money))

        if isinstance(self.user, SavingAccount):
            self.layout.addWidget(self.create_button("📈 Add Interest", self.add_interest))

        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.create_button("🔓 Logout", self.logout))

    def check_balance(self):
        QMessageBox.information(self, "Balance", f"₹{self.user.get_balance():.2f}")

    def deposit_money(self):
        amount, ok = QInputDialog.getDouble(self, "Deposit", "Amount:")
        if ok:
            deposit(self.user, amount)
            QMessageBox.information(self, "Success", f"Deposited ₹{amount:.2f}")

    def withdraw_money(self):
        amount, ok = QInputDialog.getDouble(self, "Withdraw", "Amount:")
        if ok:
            withdraw(self.user, amount)
            QMessageBox.information(self, "Success", f"Withdrew ₹{amount:.2f}")

    def add_interest(self):
        months, ok = QInputDialog.getInt(self, "Interest", "Enter number of months:")
        if ok:
            interest = self.user.intrest_rate * months * self.user.get_balance()
            self.user.deposit(interest)
            QMessageBox.information(self, "Interest Added", f"₹{interest:.2f} interest credited.")

    def logout(self):
        self.user = None
        self.clear_layout()

        # Rebuild the initial home screen
        self.title = QLabel("🏦 Welcome to Laxmi Cheat Funds")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Arial", 16, QFont.Bold))
        self.layout.addWidget(self.title)

        self.create_btn = QPushButton("➕ Create Account")
        self.create_btn.clicked.connect(self.create_account)
        self.layout.addWidget(self.wrap_button(self.create_btn))

        self.login_btn = QPushButton("🔐 Login")
        self.login_btn.clicked.connect(self.login)
        self.layout.addWidget(self.wrap_button(self.login_btn))

        self.exit_btn = QPushButton("❌ Exit")
        self.exit_btn.clicked.connect(self.close)
        self.layout.addWidget(self.wrap_button(self.exit_btn))


    def clear_layout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

# Run the application
if __name__ == '__main__':
    app = QApplication([])
    window = BankApp()
    window.show()
    app.exec_()
