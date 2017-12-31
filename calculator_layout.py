from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from style import *

mainDiv = QWidget()
mainLayout = QVBoxLayout()
Div(mainDiv, mainLayout)
mainLayout.setContentsMargins(0, 0, 0, 0)

#계산기 메인 화면
screen = QTextEdit()
screen.setReadOnly(True)
screen_result = QLineEdit()
screen_result.setReadOnly(True)
mainLayout.addWidget(screen)
mainLayout.addWidget(screen_result)

#계산기 버튼 화면
default_buttons = QVBoxLayout()
mainLayout.addLayout(default_buttons)
line_00 = QHBoxLayout()
line_01 = QHBoxLayout()
line_02 = QHBoxLayout()
line_03 = QHBoxLayout()
line_04 = QHBoxLayout()
line_05 = QHBoxLayout()

default_buttons.addLayout(line_00)
default_buttons.addLayout(line_01)
default_buttons.addLayout(line_02)
default_buttons.addLayout(line_03)
default_buttons.addLayout(line_04)
default_buttons.addLayout(line_05)

#line0

functions = QPushButton()
delete = QPushButton()
line_00.addWidget(functions)
line_00.addStretch(0)
line_00.addWidget(delete)

#line1

clean = QPushButton("Clean")
parentheses = QPushButton("()")
percent = QPushButton("%")
division = QPushButton("/")
line_01.addWidget(clean)
line_01.addWidget(parentheses)
line_01.addWidget(percent)
line_01.addWidget(division)

#line2

seven = QPushButton("7")
eight = QPushButton("8")
nine = QPushButton("9")
multiplication = QPushButton("*")
line_02.addWidget(seven)
line_02.addWidget(eight)
line_02.addWidget(nine)
line_02.addWidget(multiplication)

#line3

four = QPushButton("4")
five = QPushButton("5")
six = QPushButton("6")
minus = QPushButton("-")
line_03.addWidget(four)
line_03.addWidget(five)
line_03.addWidget(six)
line_03.addWidget(minus)

#line4

one = QPushButton("1")
two = QPushButton("2")
three = QPushButton("3")
plus = QPushButton("+")
line_04.addWidget(one)
line_04.addWidget(two)
line_04.addWidget(three)
line_04.addWidget(plus)

#line5

plus_minus = QPushButton("+/-")
zero = QPushButton("0")
dot = QPushButton(".")
result = QPushButton("=")
line_05.addWidget(plus_minus)
line_05.addWidget(zero)
line_05.addWidget(dot)
line_05.addWidget(result)

#style
screen.setStyleSheet("QTextEdit{border: none; background: #22282e; padding: 20px; font-size: 20px; color: #747a81; min-height: 100px;}")
screen_result.setStyleSheet("QLineEdit{border: none; background: #22282e; padding: 0 20px; text-align: right; color: #747a81;}")
screen_result.setAlignment(Qt.AlignRight)
line_00.setContentsMargins(0,0,0,0)
functions.setStyleSheet("QPushButton{border: none; background: none;}")
delete.setStyleSheet("QPushButton{border: none; background: none;}")
def NumberButton(entity):
    entity.setStyleSheet("""
        QPushButton{
            border: 1px solid #747a81;
            background: #23282e;
            height: 80px;
            font-weight: bold;
            font-size: 16px;
            color: #fff;
        }
    """)

NumberButton(zero)
NumberButton(one)
NumberButton(two)
NumberButton(three)
NumberButton(four)
NumberButton(five)
NumberButton(six)
NumberButton(seven)
NumberButton(eight)
NumberButton(nine)
NumberButton(plus_minus)
NumberButton(dot)

def FunctionButton(entity):
    entity.setStyleSheet("""
        QPushButton{
            border: 1px solid #747a81;
            background: #1c1f24;
            height: 80px;
            font-weight: bold;
            font-size: 16px;
            color: #8492a1;
        }
    """)

FunctionButton(clean)
FunctionButton(parentheses)
FunctionButton(percent)
FunctionButton(division)
FunctionButton(multiplication)
FunctionButton(minus)
FunctionButton(plus)

result.setStyleSheet("QPushButton{border: 1px solid #747a81; background: #fefefe; height: 80px; font-size: 16px; font-weight: bold; color: #000;}")
