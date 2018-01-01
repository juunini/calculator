import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import module
from style import Error

class Main(QMainWindow):
        def __init__(self):
                super().__init__()

                window = QWidget()
                main = QVBoxLayout()
                window.setLayout(main)
                self.setCentralWidget(window)

                window.setStyleSheet("QWidget{background: #000;color: #747a81}")
                main.setContentsMargins(50, 50, 50, 50)
                main.setSpacing(20)

                #layout area------------------------------------

                import calculator_layout as layout
                main.addWidget(layout.mainDiv)

                #layout area end------------------------------------

                #active area-----------------------------------

                def Num(number):
                    screen = layout.screen.toPlainText()
                    screenSet = layout.screen.setText
                    if len(screen) == 1 and screen == "0":
                        screenSet("")
                    elif len(screen) != 0 and screen[len(screen) - 1] == "(":
                        screenSet(screen + "*")
                    screenSet(screen + number)

                def One():
                    Num("1")
                def Two():
                    Num("2")
                def Three():
                    Num("3")
                def Four():
                    Num("4")
                def Five():
                    Num("5")
                def Six():
                    Num("6")
                def Seven():
                    Num("7")
                def Eight():
                    Num("8")
                def Nine():
                    Num("9")
                def Zero():
                    Num("0")
                def Dot():
                    screen = layout.screen.toPlainText()
                    screenSet = layout.screen.setText
                    if screen == "":
                        screenSet("0.")
                    elif screen[len(screen) - 1] == ")" or screen[len(screen) - 1] == "%":
                        screenSet(screen + "*0.")
                    elif screen[len(screen) - 1] != ")" and screen[len(screen) - 1] != "%" and screen[len(screen) - 1].isdigit() == False:
                        screenSet(screen + "0.")
                    else:
                        screenSet(screen + ".")
                def Clean():
                    layout.screen.setText("")
                    layout.screen_result.setText("")
                    global count
                    count = 0
                def Plus():
                    screen = layout.screen.toPlainText()
                    if screen == "":
                        Error("에러", "맨 처음에 수식 부호를 넣을 수 없습니다.")
                    else :
                        layout.screen.setText(screen + "＋")
                def Minus():
                    screen = layout.screen.toPlainText()
                    if screen == "":
                        Error("에러", "맨 처음에 수식 부호를 넣을 수 없습니다.")
                    else :
                        layout.screen.setText(screen + "－")
                def Multiplication():
                    screen = layout.screen.toPlainText()
                    if screen == "":
                        Error("에러", "맨 처음에 수식 부호를 넣을 수 없습니다.")
                    else :
                        layout.screen.setText(screen + "×")
                def Division():
                    screen = layout.screen.toPlainText()
                    if screen == "":
                        Error("에러", "맨 처음에 수식 부호를 넣을 수 없습니다.")
                    else :
                        layout.screen.setText(screen + "÷")
                def Percent():
                    screen = layout.screen.toPlainText()
                    if screen == "":
                        Error("에러", "%기호는 숫자 뒤에만 붙을 수 있습니다.")
                    elif screen[len(screen) - 1].isdigit() == False:
                        Error("에러", "%기호는 숫자 뒤에만 붙을 수 있습니다.")
                    else :
                        layout.screen.setText(screen + "%")
                global count
                count = 0
                def Parentheses():
                    screen = layout.screen.toPlainText()
                    global count
                    if count == 0:
                        if screen == "":
                            layout.screen.setText(screen + "(")
                            count += 1
                        elif screen[len(screen) - 1] == "%" or screen[len(screen) - 1].isdigit() == True or screen[len(screen) - 1] == ")":
                            layout.screen.setText(screen + "*(")
                            count += 1
                        else :
                            layout.screen.setText(screen + "(")
                            count += 1
                    else :
                        if screen[len(screen) - 1] == "%" or screen[len(screen) - 1] != "(" or screen[len(screen) - 1].isdigit() == True:
                            layout.screen.setText(screen + ")")
                            count -= 1
                        else :
                            layout.screen.setText(screen + "(")
                            count += 1
                def Plus_Minus():
                    screen = layout.screen.toPlainText()
                    global count
                    if screen[len(screen) - 1].isdigit() == True:
                        i = len(screen) - 1
                        while i >= 0:
                            if screen[i].isdigit() == False:
                                layout.screen.setText(screen[0 : i] + "(-" + screen[i : len(screen) - 1])
                                count += 1
                                break
                    else :
                        layout.screen.setText(screen + "(-")
                        count += 1
                def Calculate():
                    screen = layout.screen.toPlainText()
                    layout.screen.setText(layout.screen_result.text())
                    layout.screen_result.setText("")
                def DefaultCalculate():
                    copy = layout.screen.toPlainText()
                    copy = copy.replace('＋', '+').replace('－', '-').replace('×', '*').replace('÷', '/')
                    global count

                    for i in range(0, len(copy)):
                        if copy[i] == "%":
                            for j in range(i - 1, 0, -1):
                                if i == len(copy) - 1:
                                    if copy[j] != "." and copy[j].isdigit() == False:
                                        copy = copy[0 : j + 1] + str(float(copy[j + 1 : -1] / 100))
                                    else:
                                        copy = str(float(copy[0 : -1]) / 100)
                                else:
                                    if copy[j] != "." and copy[j].isdigit() == False:
                                        copy = copy[0 : j + 1] + str(float(copy[j + 1 : i] / 100)) + copy[i + 1 : len(copy)]
                                    else:
                                        copy = str(float(copy[0 : i]) / 100) + copy[i + 1 : len(copy)]

                    if copy[len(copy) - 1] == "+" or copy[len(copy) - 1] == "-" or copy[len(copy) - 1] == "*" or copy[len(copy) - 1] == "/":
                        copy = copy[0 : -1]

                    if count != 0:
                        copy = copy + ")" * count

                    if len(copy) != 0:
                        copy = str(eval(copy))

                    if copy[-2 : len(copy)] == ".0":
                        copy = copy[0 : -2]
                    layout.screen_result.setText(copy)


                layout.one.clicked.connect(One)
                layout.two.clicked.connect(Two)
                layout.three.clicked.connect(Three)
                layout.four.clicked.connect(Four)
                layout.five.clicked.connect(Five)
                layout.six.clicked.connect(Six)
                layout.seven.clicked.connect(Seven)
                layout.eight.clicked.connect(Eight)
                layout.nine.clicked.connect(Nine)
                layout.zero.clicked.connect(Zero)
                layout.dot.clicked.connect(Dot)
                layout.clean.clicked.connect(Clean)
                layout.plus.clicked.connect(Plus)
                layout.minus.clicked.connect(Minus)
                layout.multiplication.clicked.connect(Multiplication)
                layout.division.clicked.connect(Division)
                layout.percent.clicked.connect(Percent)
                layout.parentheses.clicked.connect(Parentheses)
                layout.plus_minus.clicked.connect(Plus_Minus)
                layout.screen.textChanged.connect(DefaultCalculate)
                layout.result.clicked.connect(Calculate)

                #active area end---------------------------------
                #크기 설정
                self.setGeometry(300,100,480,0)
                #제목 설정
                self.setWindowTitle("계산기");
                self.show()

if __name__ == "__main__":
        app = QApplication(sys.argv)
        do = Main()
        sys.exit(app.exec_())
