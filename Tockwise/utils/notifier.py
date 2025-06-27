from PyQt5.QtWidgets import QMessageBox

def show_notification(title, message):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.exec_()
