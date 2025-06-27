from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from core.db import check_user_credentials

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TockWise - Login")
        self.setGeometry(100, 100, 300, 150)
        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        layout.addWidget(QLabel("Login to TockWise"))
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        if check_user_credentials(email, password):
            QMessageBox.information(self, "Success", "Login successful!")
        else:
            QMessageBox.critical(self, "Error", "Invalid credentials")
