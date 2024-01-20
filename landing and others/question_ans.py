# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\question_ans.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from random import sample,shuffle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 375)
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
        icon1.addPixmap(QtGui.QPixmap(":/icons/New folder/airplay.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/New folder/award.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/New folder/coffee.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/New folder/music.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/New folder/wifi.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.timer_label = QtWidgets.QLabel(self.main_body)
        self.timer_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.timer_label.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:600;\n"
"font-size:28px;")
        self.timer_label.setObjectName("timer_label")
        self.verticalLayout_6.addWidget(self.timer_label)
        self.question_label = QtWidgets.QLabel(self.main_body)
        self.question_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.question_label.setStyleSheet(" font-family: \'Istok Web\';\n"
"\n"
"font-weight:600;\n"
"font-size:34px;")
        self.question_label.setAlignment(QtCore.Qt.AlignCenter)
        self.question_label.setObjectName("question_label")
        self.verticalLayout_6.addWidget(self.question_label)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.option_1 = QtWidgets.QRadioButton(self.main_body)
        self.option_1.setMinimumSize(QtCore.QSize(0, 80))
        self.option_1.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:500;\n"
"font-size:26px;\n"
"margin-left:20px;")
        self.option_1.setObjectName("option_1")
        self.verticalLayout_5.addWidget(self.option_1)
        self.option_2 = QtWidgets.QRadioButton(self.main_body)
        self.option_2.setMinimumSize(QtCore.QSize(0, 80))
        self.option_2.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:500;\n"
"font-size:26px;\n"
"margin-left:20px;")
        self.option_2.setObjectName("option_2")
        self.verticalLayout_5.addWidget(self.option_2)
        self.option_3 = QtWidgets.QRadioButton(self.main_body)
        self.option_3.setMinimumSize(QtCore.QSize(0, 80))
        self.option_3.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:500;\n"
"font-size:26px;\n"
"margin-left:20px;")
        self.option_3.setObjectName("option_3")
        self.verticalLayout_5.addWidget(self.option_3)
        self.option_4 = QtWidgets.QRadioButton(self.main_body)
        self.option_4.setMinimumSize(QtCore.QSize(0, 80))
        self.option_4.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:500;\n"
"font-size:26px;\n"
"margin-left:20px;")
        self.option_4.setObjectName("option_4")
        self.verticalLayout_5.addWidget(self.option_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.next_button = QtWidgets.QPushButton(self.main_body)
        self.next_button.setMinimumSize(QtCore.QSize(0, 80))
        self.next_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_button.setMouseTracking(False)
        self.next_button.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:600;\n"
"font-size:18px;\n"
"background-color: rgb(27, 239, 52);\n"
"border-radius:7px;")
        
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(self.timer_timeout)
        self.time_left = 15  # Initial time (seconds)
        self.timer.start(1000) 
        self.next_button.setObjectName("next_button")
        self.verticalLayout_6.addWidget(self.next_button)
        self.horizontalLayout.addWidget(self.main_body)
        self.main_body.raise_()
        self.side_menu.raise_()
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.next_button.clicked.connect(self.next_question)
        self.questions = [
            [
                "Which planet is known as the \"Red Planet\"?", "a) Venus", "b) Mars", "c) Jupiter", "d) Saturn", "b"
            ],
            [
                "Who painted the famous artwork \"The Mona Lisa\"?", "a) Pablo Picasso", "b) Leonardo da Vinci",
                "c) Vincent van Gogh", "d) Claude Monet", "b"
            ],
            [
                "What is the chemical symbol for gold?", "a) Go", "b) Gd", "c) Au", "d) Ag", "c"
            ],
            [
                "What is the 2nd tallest mountain in the world?", "a) Mount Everest", "b) K2",
                "c) Mount Kilimanjaro", "d) Mount McKinley", "b"
            ],
            [
                "What is the chemical symbol for Scandium?", "a) Sn", "b) Scan", "c) Sd", "d) Sc", "d"
            ],
            [
                "What is the capital of France?", "a) London", "b) Paris", "c) Berlin", "d) Rome", "b"
            ],  
                [
                "Who wrote \"Romeo and Juliet\"?", "a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen", "d) Mark Twain", "b"
            ],
            [
                "What is the largest mammal in the world?", "a) Elephant", "b) Giraffe", "c) Blue Whale", "d) Lion", "c"
            ],
            [
                "In which year did Christopher Columbus discover America?", "a) 1492", "b) 1588", "c) 1776", "d) 1620", "a"
            ],
            [
                "What is the chemical symbol for water?", "a) W", "b) O", "c) H2O", "d) Wa", "c"
            ],
            [
                "Who is known as the \"Father of Computers\"?", "a) Bill Gates", "b) Alan Turing", "c) Steve Jobs", "d) Charles Babbage", "d"
            ],
            [
                "What is the currency of Japan?", "a) Won", "b) Ringgit", "c) Yen", "d) Baht", "c"
            ],
            [
                "What is the square root of 64?", "a) 6", "b) 7", "c) 8", "d) 9", "c"
            ],
            [
                "Who painted the Mona Lisa?", "a) Vincent van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci", "d) Claude Monet", "c"
            ]
]

        self.selected_questions = sample(self.questions, 7)
        self.current_question = 0
        self.user_answers = []

        self.show_question()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def show_question(self):
        if self.current_question < len(self.selected_questions):
            question_data = self.selected_questions[self.current_question]
            self.question_label.setText(question_data[0])

            options = question_data[1:5]
            

            for i in range(4):
                getattr(self, f"option_{i+1}").setText(options[i])

            self.timer_label.setText(f'Time remaining: {self.time_left} seconds')

            self.timer.start()

        else:
            self.evaluate_answers()
    def next_question(self):
        self.timer.stop()
        selected_option = None

        for i in range(4):
            if getattr(self, f"option_{i+1}").isChecked():
                selected_option = chr(ord('a') + i)

        if selected_option is not None:
            self.user_answers.append(selected_option)
        else:
            self.user_answers.append('')  # Mark unanswered question

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.time_left = 15  # Reset timer for each new question
            self.show_question()
            self.timer.start()
        else:
            self.evaluate_answers()
        
    def evaluate_answers(self):
        correct_answers = sum(user_ans == question[-1] for user_ans, question in zip(self.user_answers, self.selected_questions))
        total_questions = len(self.selected_questions)

        QMessageBox.information(MainWindow, 'Results', f'You answered {correct_answers} out of {total_questions} questions correctly.')
        MainWindow.close()  
            
    def timer_timeout(self):
        self.time_left -= 1
        self.timer_label.setText(f'Time remaining: {self.time_left} seconds')

        if self.time_left == 0:
            self.timer.stop()
            current_question_index = self.current_question
            self.user_answers.append('')  # Mark unanswered question
            QMessageBox.warning(MainWindow, "Time's Up!", 'You did not respond in time. Moving to the next question.')

            # Mark the previous unanswered question as incorrect
            if current_question_index < len(self.questions):
                self.user_answers[current_question_index] = 'incorrect'

            self.current_question += 1
            if self.current_question < len(self.questions):
                self.time_left = 15  # Reset timer for each new question
                self.show_question()
                self.timer.start()
            else:
                self.evaluate_answers()

                   
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
        self.timer_label.setText(_translate("MainWindow", "Timer Count down here"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
