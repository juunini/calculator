from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def Div(entity, layout):
    entity.setLayout(layout)
    entity.setStyleSheet("QWidget{background: #22282e; color: #747a81;}")
    layout.setContentsMargins(0, 0, 0, 40)
    layout.setSpacing(0)

def Title(div, layout, stat, title, statmsg, titlemsg):
    div.setLayout(layout)
    stat.setText(statmsg)
    title.setText(titlemsg)
    layout.addWidget(stat)
    layout.addWidget(title)
    layout.addStretch(0)
    div.setStyleSheet("QWidget{padding: 0 30px; background: qlineargradient(x1:0 y1:0 x2:0 y2:1, stop:0 #23282e, stop:1 #1c1f24);}")
    div.setFixedHeight(90)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)
    stat.setStyleSheet("QLabel{font-size: 28px; font-weight: light; color: #fff; background: none; font-family: Sansita, sans-serif}")
    title.setStyleSheet("QLabel{margin-top: 14px; font-size: 16px; font-weight: bold; font-family: NanumGothic, sans-serif; color: #8492a1; background: none;}")

def Input(entity, layout):
    layout.addWidget(entity)
    entity.setStyleSheet("QLineEdit{height: 30px;padding: 0 20px;font-size: 14px;font-family: Sansita, sans-serif;color: #747a81;border-top: 2px solid #101315;border-left: 2px solid #101315;border-right: 2px solid #242a2f;border-bottom: 2px solid #2b3136;background: #15181b;}")

def TextArea(entity, layout):
    layout.addWidget(entity)
    entity.setStyleSheet("QTextEdit{height: 90px;padding: 0 20px;font-size: 14px;font-family: Sansita, sans-serif;color: #747a81;border-top: 2px solid #101315;border-left: 2px solid #101315;border-right: 2px solid #242a2f;border-bottom: 2px solid #2b3136;background: #15181b;}")

def Select(entity, layout):
    layout.addWidget(entity)
    entity.setStyleSheet("QComboBox{height: 30px;padding: 0 20px;font-size: 14px;color: #747a81;border-top: 2px solid #101315;border-left: 2px solid #101315;border-right: 2px solid #242a2f;border-bottom: 2px solid #2b3136;background: #15181b;font-family: Sansita, sans-serif;}QComboBox::drop-down{border: none;}QComboBox::down-arrow{width: 0;height: 0;margin-top: 4px;margin-right: 10px;border: 5px solid #15181b;border-top: 5px solid #747a81;}QComboBox QAbstractItemView{border: 2px solid #101315;}")

def Button1(entity, msg, layout):
    layout.addWidget(entity)
    entity.setText(msg)
    entity.setStyleSheet("QPushButton{min-width: 180px; min-height: 70px; color: #fff; font-size: 18px; font-weight: bold; font-family: Sansita, sans-serif; background: #cd70ff;}")

def Button2(entity, msg, layout):
    layout.addWidget(entity)
    entity.setText(msg)
    entity.setStyleSheet("QPushButton{min-width: 180px; min-height: 70px; color: #fff; font-size: 18px; font-weight: bold; font-family: Sansita, sans-serif; background: #11beff;}")

def Error(title, text):
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText(text)
	msg.setWindowTitle(title)

	msg.setStandardButtons(QMessageBox.Ok)

	msg.setStyleSheet("""
        QMessageBox{background: #22282e;}
        QLabel{margin-top: 10px;margin-bottom: 10px;font-size: 16px;font-family: NanumGothic, sans-serif;color: #747a81;}
        PushButton{min-width: 90px;min-height: 35px;color: #fff;font-size: 18px;font-weight: bold;font-family: Sansita;background: #ce70ff;}
	""")

	msg.show()
	msg.exec_()
