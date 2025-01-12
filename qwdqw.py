from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QMessageBox,QRadioButton,QHBoxLayout
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Dota2')

title = QLabel('wd')
question = QLabel('в каком году')
btn_answer1 = QRadioButton('2013')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2016')
btn_answer4 = QRadioButton('2019')
btn_answer = QRadioButton('Подпись')

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2,alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer3,alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer4,alignment=Qt.AlignCenter)
layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)


v_line = QVBoxLayout()
v_line.addWidget(title,alignment=Qt.AlignCenter)
main_win.setLayout((v_line))












def show_win():
    victory_win = QMessageBox()
    victory_win.setText('верно')
    victory_win.exec_()



def show_lose():
    victory_wi2n = QMessageBox()
    victory_wi2n.setText('не верно')
    victory_wi2n.exec_()



btn_answer3.clicked.connect(show_win)
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)

main_win.show()
app.exec_()
