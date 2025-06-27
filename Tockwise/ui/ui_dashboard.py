from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TockWise Dashboard")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to TockWise Dashboard!"))
        self.setLayout(layout)
