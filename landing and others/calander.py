# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calander.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 401)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
"  border: none;\n"
"  background-color: transparent;\n"
"  color: #FFF; /* Specify a default color */\n"
"}\n"
"\n"
"#centralwidget {\n"
"  background-color: white\n"
";\n"
"}\n"
"\n"
"#side_menu {\n"
"  background-color: #071e26;\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  padding: 10px;\n"
"  background-color: #071e26;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"#main_body {\n"
"  background-color: #071e26;\n"
"  border-radius: 10px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 50))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.header)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons_folder/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QWidget(self.frame_2)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.side_menu)
        self.frame_4.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons_folder/airplay.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons_folder/award.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons_folder/bar-chart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons_folder/cloud-drizzle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons_folder/crosshair.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_body = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.gridLayout = QtWidgets.QGridLayout(self.main_body)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_6 = QtWidgets.QFrame(self.main_body)
        self.frame_6.setStyleSheet("background-color:transprent;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_6)
        self.calendarWidget.setStyleSheet("color: rgb(85, 255, 255);\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font-family: \'Istok Web\';")
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_6.addWidget(self.calendarWidget)
        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.main_body)
        self.frame_5.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.addButton = QtWidgets.QPushButton(self.frame_5)
        self.addButton.setMinimumSize(QtCore.QSize(10, 0))
        self.addButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.addButton.setBaseSize(QtCore.QSize(0, 0))
        self.addButton.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"font-family: \'Istok Web\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size:12 px;\n"
"color:#071e26;\n"
"border-radius:5px\n"
"\n"
"\n"
"")
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_5.addWidget(self.addButton)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"font-family: \'Istok Web\';\n"
"border-radius:5px;\n"
"letter-spacing:1px;\n"
"font-szie:6px;\n"
"padding-left:4px")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.tasksListWidget = QtWidgets.QListWidget(self.frame_5)
        self.tasksListWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;")
        self.tasksListWidget.setObjectName("tasksListWidget")
        item = QtWidgets.QListWidgetItem()
        self.tasksListWidget.addItem(item)
        self.verticalLayout_5.addWidget(self.tasksListWidget)
        self.saveButton = QtWidgets.QPushButton(self.frame_5)
        self.taskLineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.verticalLayout_5.addWidget(self.taskLineEdit)
        self.saveButton.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"font-family: \'Istok Web\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size:12 px;\n"
"color:#071e26;\n"
"\n"
"\n"
"\n"
"")
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_5.addWidget(self.saveButton)
        self.gridLayout.addWidget(self.frame_5, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.main_body)
        self.main_body.raise_()
        self.side_menu.raise_()
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menu_expanded = False

        # Connect the button click event to the toggle_menu function
        self.pushButton.clicked.connect(self.toggle_menu)

        # Set up the animation for the side menu
        self.side_menu_animation = QtCore.QPropertyAnimation(self.side_menu, b"maximumWidth")
        self.side_menu_animation.setDuration(300)

        # Set up the central widget animation for overlay effect
        self.central_widget_animation = QtCore.QPropertyAnimation(self.centralwidget, b"geometry")
        self.central_widget_animation.setDuration(300)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.conn = sqlite3.connect('C:\\Users\\pande\\OneDrive\\Desktop\\Feb-7 Project\\landing and others\\data.db')
        self.cursor = self.conn.cursor()
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
    def calendarDateChanged(self):
            print("The calendar date was changed.")
            dateSelected = self.calendarWidget.selectedDate().toPyDate()
            print("Date selected:", dateSelected)
            self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.tasksListWidget.clear()

        query = "SELECT task, completed FROM tasks WHERE date = ?"
        row = (date,)
        results = self.cursor.execute(query, row).fetchall()
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(Qt.Unchecked)
            self.tasksListWidget.addItem(item)

    def saveChanges(self):
        date = self.calendarWidget.selectedDate().toPyDate()

        for i in range(self.tasksListWidget.count()):
            item = self.tasksListWidget.item(i)
            task = item.text()
            if item.checkState() == Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task, date,)
            self.cursor.execute(query, row)
        self.conn.commit()

        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def addNewTask(self):
        newTask = str(self.lineEdit.text())  # Use self.lineEdit.text() instead of self.taskLineEdit.text()
        date = self.calendarWidget.selectedDate().toPyDate()

        query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
        row = (newTask, "NO", date,)

        try:
            self.cursor.execute(query, row)
            self.conn.commit()
            self.updateTaskList(date)
            self.lineEdit.clear()  # Clear the lineEdit widget
        except Exception as e:
            print(f"An error occurred: {e}")


    def closeEvent(self, event):
        self.conn.close()
        event.accept()
    def toggle_menu(self):
        # Toggle the menu state
        self.menu_expanded = not self.menu_expanded

        # Define the target width for the side menu
        target_width = 200 if self.menu_expanded else 0

        # Update the side menu animation
        self.side_menu_animation.setEndValue(target_width)
        self.side_menu_animation.start()

        # Update the central widget animation for overlay effect
        if self.menu_expanded:
            self.central_widget_animation.setEndValue(QtCore.QRect(200, 0, 586, 370))
        else:
            self.central_widget_animation.setEndValue(QtCore.QRect(0, 0, 586, 370))
        self.central_widget_animation.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "Samadhan App"))
        self.pushButton_2.setText(_translate("MainWindow", "Item 1"))
        self.pushButton_3.setText(_translate("MainWindow", "Item 2"))
        self.pushButton_4.setText(_translate("MainWindow", "Item 3"))
        self.pushButton_5.setText(_translate("MainWindow", "Item 4"))
        self.pushButton_6.setText(_translate("MainWindow", "Item 5"))
        self.pushButton_17.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_18.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_19.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_16.setText(_translate("MainWindow", "PushButton"))
        self.label_4.setText(_translate("MainWindow", "Academic Supervison"))
        self.label_5.setText(_translate("MainWindow", "Academic Anaysis"))
        self.label_7.setText(_translate("MainWindow", "     Time Effecient"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "My app"))
        self.pushButton_2.setText(_translate("MainWindow", "Item 1"))
        self.pushButton_3.setText(_translate("MainWindow", "Item 2"))
        self.pushButton_4.setText(_translate("MainWindow", "Item 3"))
        self.pushButton_5.setText(_translate("MainWindow", "Item 4"))
        self.pushButton_6.setText(_translate("MainWindow", "Item 5"))
        self.addButton.setText(_translate("MainWindow", "Add New"))
        __sortingEnabled = self.tasksListWidget.isSortingEnabled()
        self.tasksListWidget.setSortingEnabled(False)
        item = self.tasksListWidget.item(0)
        item.setText(_translate("MainWindow", "hello"))
        self.tasksListWidget.setSortingEnabled(__sortingEnabled)
        self.saveButton.setText(_translate("MainWindow", "Save Changes"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
