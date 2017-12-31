from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def Calculate_Function(function, entity):
    copy = entity
    i = len(copy) - 1
    while i > 0:
        global start
        global end
        start = 0
        end = 0
        if copy[i] == function:
            j = i - 1
            while j > 0:
                if copy[j] != "." and copy[j].isdigit() == False:
                    start = j + 1
                    break
                elif j == 1 and copy[j].isdigit() == True:
                    start = 0
                j -= 1

            #start가 0이면 수식어 앞쪽으로는 전부 숫자.

            if i == len(copy) - 1:
                end = 0
            else:
                j = i + 1
                while j < len(copy):
                    if copy[j] != "." and copy[j].isdigit() == False and j != len(copy) - 1:
                        end = j
                        break
                    elif j == len(copy) - 1 :
                        end = len(copy)
                    j += 1

            #end가 0인 경우는 수식이 맨 끝에 있을 때.

        if start == 0 and end == 0:    #수식 앞에 수식 없고 수식이 맨 끝에 있을 때
            copy = copy[0 : -1]
        elif start == 0 and end != 0:   #수식 앞에 수식 없고 수식 뒤에 수식이 있을 때
            if function == "+":
                copy = str(float(copy[0 : i]) + float(copy[i + 1 : end]))
            elif function == "-":
                copy = str(float(copy[0 : i]) - float(copy[i + 1 : end]))
            elif function == "*":
                copy = str(float(copy[0 : i]) * float(copy[i + 1 : end]))
            elif function == "/":
                copy = str(float(copy[0 : i]) / float(copy[i + 1 : end]))
        elif start != 0 and end == 0:   #수식 앞에 수식이 있고, 수식이 맨 끝에 있을 때
            copy = copy[0 : -1]
        elif start != 0 and end != 0:   #수식 앞 뒤로 다 수식이 있을 때
            if function == "+":
                if copy[start - 1] == "-":  #앞 수식이 -인 경우
                    if float(copy[start - 1 : i]) + float(copy[i + 1 : end]) > 0:   #-까지 더 해서 수식의 결과가 0보다 클 때
                        copy = copy[0 : start - 1] + "+" + str(float(copy[start - 1 : i]) + float(copy[i + 1 : end])) + copy[end : len(copy)]
                    elif float(copy[start - 1 : i]) + float(copy[i + 1 : end]) < 0:     #-까지 더 해서 수식의 결과가 0보다 작을 때
                        copy = copy[0 : start - 1] + str(float(copy[start - 1 : i]) + float(copy[i + 1 : end])) + copy[end : len(copy)]
                    else:   #-까지 더 해서 수식의 결과가 0일 때
                        copy = copy[0 : start - 1] + copy[end : len(copy)]
                else:   #앞 수식이 -가 아닌 경우
                    copy = copy[0 : start] + str(float(copy[start : i]) + float(copy[i + 1 : end])) + copy[end : len(copy)]

            elif function == "-":
                if copy[start - 1] == "-":  #앞 수식이 -인 경우
                    if float(copy[start - 1 : i]) - float(copy[i + 1 : end]) != 0:     #수식의 결과가 0이 아닐 때
                        copy = copy[0 : start - 1] + str(float(copy[start - 1 : i]) - float(copy[i + 1 : end])) + copy[end : len(copy)]
                    else:   #수식의 결과가 0일 때
                        copy = copy[0 : start - 1] + copy[end : len(copy)]
                else:   #앞 수식이 -가 아닌 경우
                    copy = copy[0 : start] + str(float(copy[start : i]) - float(copy[i + 1 : end])) + copy[end : len(copy)]

            elif function == "*":
                if copy[start - 1] == "-":  #앞 수식이 -인 경우
                    copy = copy[0 : start - 1] + str(float(copy[start - 1 : i]) * float(copy[i + 1 : end])) + copy[end : len(copy)]
                else:   #앞 수식이 -가 아닌 경우
                    copy = copy[0 : start] + str(float(copy[start : i]) * float(copy[i + 1 : end])) + copy[end : len(copy)]

            elif function == "/":
                if copy[start - 1] == "-":  #앞 수식이 -인 경우
                    copy = copy[0 : start - 1] + str(float(copy[start - 1 : i]) / float(copy[i + 1 : end])) + copy[end : len(copy)]
                else:   #앞 수식이 -가 아닌 경우
                    copy = copy[0 : start] + str(float(copy[start : i]) / float(copy[i + 1 : end])) + copy[end : len(copy)]

            i = len(copy) - 1   #연산을 실행했으면 처음부터 다시 확인하며 다시 연산자가 나오면 수행.
        i -= 1
    return copy

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

def Do_Calculate(entity):
    copy = Percent_Calculate(entity)
    copy = Calculate_Function("/", copy)
    copy = Calculate_Function("*", copy)
    copy = Calculate_Function("-", copy)
    copy = Calculate_Function("+", copy)
    return copy

def Calculate(entity):    #괄호 연산 알고리즘(종합 연산)
    copy = entity
    open_ = []
    close_ = []
    i = len(copy) - 1
    while i >= 0:
        if copy[i] == ")":  #닫는 괄호를 찾는다.
            close_.append(i)

        elif copy[i] == "(":  #여는 괄호를 찾는다.
            open_.append(i)

            if len(close_) == 0:    #닫는 괄호가 없는경우
                cal = copy[open_[0] + 1 : len(copy)]
                cal = Do_Calculate(cal)   #여는 괄호 이후의 연산을 모두 계산.
                copy = copy[0 : open_[0]] + str(cal)    #괄호의 값을 리턴하며 여는괄호 하나 제거
            else:   #닫는 괄호가 있는 경우
                if len(close_) == 1 and close_[0] == len(copy) - 1:     #닫는 괄호가 하나만 있고 맨 끝에 있는 경우
                    cal = copy[open_[0] + 1 : -1]
                    cal = Do_Calculate(cal)
                    copy = copy[0 : open_[len(open_) - 1]] + str(cal)
                #elif len(close_) == 1 and close_[0] != len(copy) -1:    #닫는 괄호가 하나만 있고 맨 끝에 있지 않은 경우
                #    cal = copy[open_[0] + 1 : close_[0]]
                #    Do_Calculate(cal)
                #    copy = copy[0 : open_[len(open_) - 1]] + str(cal) + copy[close_[0] + 1 : len(copy)]
                else:   #닫는 괄호가 여러개 있는 경우
                    cal = copy[open_[0] + 1 : close_[len(close_) - 1]]
                    cal = Do_Calculate(cal)
                    copy = copy[0 : open_[len(open_) - 1]] + str(cal) + copy[close_[len(close_) - 1] + 1 : len(copy)]

            open_ = []
            close_ = []
            i = len(copy) - 1   #다시 처음부터 괄호 확인

        i -= 1
    copy = Do_Calculate(copy)

    return copy

