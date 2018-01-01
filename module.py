from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def Percent_Calculate(entity):
    copy = entity
    i = len(copy) - 1
    while i > 0:
        if copy[i] == "%":  # %기호를 찾았을 때
            j = i - 1
            while j > 0:
                if copy[j].isdigit() == False and copy[j] != ".":   #중간에 수식이 있는 경우
                    cal = copy[j + 1 : i + 1]
                    copy = copy[0 : j + 1] + str(float(copy[j + 1 : i]) / 100) + copy[i + 1 : len(copy)]
                    i = len(copy) - 1   #다시 수행
                    break
                elif j == 1 and copy[j].isdigit() == True or copy[j] == ".":    #맨 처음까지 수식이 없을 때
                    copy = str(float(copy[0 : i]) / 100) + copy[i + 1 : len(copy)]
        i -= 1
    return copy

def Calculate(entity):    #괄호 연산 알고리즘(종합 연산)
    copy = entity
    copy = copy.replace('＋', '+').replace('－', '-').replace('×', '*').replace('÷', '/')
    if copy[len(copy) - 1] == "+" or copy[len(copy) - 1] == "-" or copy[len(copy) - 1] == "*" or copy[len(copy) - 1] == "/":
        copy = copy[0 : -1]
    elif count != 0:
        copy = copy + ")" * count
        count = 0

    if copy[-2 : len(copy)] == ".0":
        copy = copy[0 : -2]
    return copy
