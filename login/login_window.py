import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMessageBox, QStackedWidget, QMainWindow
from PyQt5.uic import loadUi
import stripes_rc
from landing import LandingPage


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):  
        loadUi("myapp/Resources/loginui.ui", self)
        self.signup_tab = self.findChild(QPushButton, "signup")
        self.login_button = self.findChild(QPushButton, "Login_button")
        self.login_username = self.findChild(QLineEdit, "username")
        self.login_password = self.findChild(QLineEdit, "username_2")

        # Connect the signal after loading the UI
        self.login_button.clicked.connect(self.login_button_clicked)
        self.signup_tab.clicked.connect(self.signup_clicked)
        
        # Add the following line to set the layout for the main window
        self.setLayout(self.layout())

    def login_button_clicked(self):
        username = self.login_username.text()
        password = self.login_password.text()

        # Add your login validation logic here
        if self.check_credentials(username, password):
                # self.show_message("Login Successful")
                landing = LandingPage()
                widget.addWidget(landing)
                widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            self.show_message("Login Failed")

    def check_credentials(self, username, password):
        connection = sqlite3.connect("studentapp.db")
        cursor = connection.cursor()

        # Check if the username and password match a record in the database
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        connection.close()

        return user is not None

    def signup_clicked(self):
        signupwin = SignupWindow()
        widget.addWidget(signupwin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def show_message(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Info")
        msg.exec_()


class SignupWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        loadUi("myapp/Resources/signupui.ui", self)
        self.signup_button = self.findChild(QPushButton, "Login_button")
        self.logintab_button = self.findChild(QPushButton, "Login")
        self.username_signup = self.findChild(QLineEdit, "username")
        self.line_password = self.findChild(QLineEdit, "username_2")
        self.line_email = self.findChild(QLineEdit, "username_3")
        self.line_contact = self.findChild(QLineEdit, "username_4")

        # Connect the signal after loading the UI
        self.signup_button.clicked.connect(self.on_signup)
        self.logintab_button.clicked.connect(self.login_clicked)
        
    def login_clicked(self):
        loginwin = Ui_MainWindow()
        widget.addWidget(loginwin)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def on_signup(self):
        username = self.username_signup.text()
        password = self.line_password.text()
        email = self.line_email.text()
        contact = self.line_contact.text()

        connection = sqlite3.connect('studentapp.db')
        cursor = connection.cursor()

        # Check if the user already exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            QMessageBox.warning(self, 'Signup Error', 'Username already exists. Please choose a different one.')
        else:
            # Insert the new user
            cursor.execute('INSERT INTO users (username, password,email,contact) VALUES (?, ?, ?, ?)',
                           (username, password, email, contact))
            connection.commit()
            connection.close()

            QMessageBox.information(self, 'Signup Successful', 'Account created for {}'.format(username))

    def login_window_closed(self):
        # Re-enable the signup window when the login window is closed
        self.setDisabled(False)

    def reset_ui(self):
        # Reset UI components as needed
        self.username_signup.clear()
        self.line_password.clear()
        self.line_email.clear()
        self.line_contact.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    MainWindow = Ui_MainWindow()
    widget.addWidget(MainWindow)

    # Set the size of the QStackedWidget to match the default size of the UI
    widget.setFixedWidth(MainWindow.width())
    widget.setFixedHeight(MainWindow.height())

    widget.show()
    sys.exit(app.exec_())
