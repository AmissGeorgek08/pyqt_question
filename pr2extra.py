from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QMessageBox, QRadioButton

def question_def():
    app = QApplication([])
    main_win = QWidget()
    main_win.setWindowTitle('Quiz')

    question = QLabel()

    btn_answer1 = QRadioButton()
    btn_answer2 = QRadioButton()
    btn_answer3 = QRadioButton()
    btn_answer4 = QRadioButton()

    question.setText("What year did the channel recieve the ''gold play button'' from YouTube?")

    btn_answer1.setText("2005")
    btn_answer2.setText("2010")
    btn_answer3.setText("2015")
    btn_answer4.setText("2020")

    layoutH1 = QHBoxLayout()
    layoutH2 = QHBoxLayout()
    layoutH3 = QHBoxLayout()

    layoutH1.addWidget(question, alignment = Qt.AlignCenter)
    layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
    layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
    layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
    layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)

    layout_main = QVBoxLayout()

    layout_main.addLayout(layoutH1)
    layout_main.addLayout(layoutH2)
    layout_main.addLayout(layoutH3)

    main_win.setLayout(layout_main)

    btn_answer3.clicked.connect(show_win)
    btn_answer1.clicked.connect(show_lose)
    btn_answer2.clicked.connect(show_lose)
    btn_answer4.clicked.connect(show_lose)

    main_win.setLayout(layout_main)
    main_win.resize(400, 250)
    main_win.show()
    app.exec_()

def show_win():
    victory_win = QMessageBox()
    victory_win.setWindowTitle('Answer:')
    victory_win.setText('Correct!\nYou win a gyro scooter')
    victory_win.exec_()
def show_lose():
    victory_win = QMessageBox()
    victory_win.setWindowTitle('Answer:')
    victory_win.setText('Wrong!\nYou win a company poster')
    victory_win.exec_()

question_def()

'''question2.setText("What color is Darth Vader's lightsaber?")
btn2_answer1.setText('Green')
btn2_answer2.setText('Purple')
btn2_answer3.setText('Red')
btn2_answer4.setText('Blue')

question3.setText("How many people live on Earth?")
btn3_answer1.setText('20 Billion')
btn3_answer2.setText('17 Billion')
btn3_answer3.setText('8 Billion')
btn3_answer4.setText('7 Billion')

question4.setText("What's 9 + 10?")
btn4_answer1.setText('21')
btn4_answer2.setText('19')
btn4_answer3.setText('910')
btn4_answer4.setText('109')'''