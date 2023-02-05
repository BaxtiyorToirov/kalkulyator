from PyQt5.QtWidgets import QApplication,QWidget,QLabel, QLineEdit,QPushButton
from PyQt5.QtGui import QIcon,QFont
import sys

class funk:
    def __init__(self):
        self.text=""
        self.lst=[]
    def funk_nol(self):
        self.text+="0"
        bir.setText(self.text)
    def funk_bir(self):
        self.text+="1"
        bir.setText(self.text)
    def funk_ikki(self):
        self.text+="2"
        bir.setText(self.text)
    def funk_uch(self):
        self.text+="3"
        bir.setText(self.text)
    def funk_turt(self):
        self.text+="4"
        bir.setText(self.text)
    def funk_besh(self):
        self.text+="5"
        bir.setText(self.text)
    def funk_olti(self):
        self.text+="6"
        bir.setText(self.text)
    def funk_yetti(self):
        self.text+="7"
        bir.setText(self.text)
    def funk_sakkiz(self):
        self.text+="8"
        bir.setText(self.text)
    def funk_tuqqiz(self):
        self.text+="9"
        bir.setText(self.text)
    def funk_qaytar(self):
        self.text=self.text[:-1]
        bir.setText(self.text)
    def funk_uchir(self):
        self.text=""
        bir.setText(self.text)
    def funk_kupaytir(self):
        self.text+="*"
        bir.setText(self.text)
    def funk_bulish(self):
       self.text+="/"
       bir.setText(self.text)
    def funk_qushish(self):
       self.text+="+"
       bir.setText(self.text)
    def funk_ayirish(self):
       self.text+="-"
       bir.setText(self.text)
    def funk_teng(self):
       bir.setText(str(eval(self.text)))
    def funk_pl_mn(self):
        self.lst.extend(self.text)

        print(self.lst)
        if self.lst[0]=="-":
            self.lst.pop(0)
            self.text=""
            for i in self.lst:
                self.text+=i
        else:
            pass
        bir.setText(self.text)
        self.lst.clear()
    def funk_vergul(self):
        self.text+="."
        bir.setText(self.text)
    
app=QApplication([])
widget=QWidget()
widget.setFixedSize(300,400)

kitob=QLabel("",widget)
kitob.setFont(QFont("Times",16))
obj=funk()


bir=QLineEdit(widget)
bir.setGeometry(10,20,280,50)
bir.setFont(QFont("Times",16))
bir.setPlaceholderText("0")

tugma1=QPushButton("c",widget)
tugma1.setGeometry(10,90,50,50)
tugma1.setFont(QFont("Times",10))
tugma1.clicked.connect(obj.funk_uchir)

tugma2=QPushButton("<-",widget)
tugma2.setGeometry(80,90,50,50)
tugma2.setFont(QFont("Times",10))
tugma2.clicked.connect(obj.funk_qaytar)

tugma4=QPushButton("*",widget)
tugma4.setGeometry(240,90,50,50)
tugma4.setFont(QFont("Times",10))
tugma4.clicked.connect(obj.funk_kupaytir)

tugma5=QPushButton("7",widget)
tugma5.setGeometry(10,150,50,50)
tugma5.setFont(QFont("Times",10))



def bos():
    
    bir.setText(tugma5.text())
    bir.adjustSize()
tugma5.clicked.connect(obj.funk_yetti)
tugma5.setStyleSheet("color:black;background-color:white")

tugma6=QPushButton("8",widget)
tugma6.setGeometry(80,150,50,50)
tugma6.setFont(QFont("Times",10))
def bos():
    bir.setText("8")
    bir.adjustSize()
tugma6.clicked.connect(obj.funk_sakkiz)
tugma6.setStyleSheet("color:black;background-color:white")

tugma7=QPushButton("9",widget)
tugma7.setGeometry(150,150,50,50)
tugma7.setFont(QFont("Times",10))
def bos():
    bir.setText("9")
    bir.adjustSize()
tugma7.clicked.connect(obj.funk_tuqqiz)
tugma7.setStyleSheet("color:black;background-color:white")

tugma8=QPushButton("/",widget)
tugma8.setGeometry(240,150,50,50)
tugma8.setFont(QFont("Times",10))
tugma8.clicked.connect(obj.funk_bulish)

tugma9=QPushButton("4",widget)
tugma9.setGeometry(10,210,50,50)
tugma9.setFont(QFont("Times",10))
def bos():
    bir.setText("4")
    bir.adjustSize()
tugma9.clicked.connect(obj.funk_turt)
tugma9.setStyleSheet("color:black;background-color:white")

tugma10=QPushButton("5",widget)
tugma10.setGeometry(80,210,50,50)
tugma10.setFont(QFont("Times",10))
def bos():
    bir.setText("5")
    bir.adjustSize()
tugma10.clicked.connect(obj.funk_besh)
tugma10.setStyleSheet("color:black;background-color:white")

tugma11=QPushButton("6",widget)
tugma11.setGeometry(150,210,50,50)
tugma11.setFont(QFont("Times",10))
def bos():
    bir.setText("6")
    bir.adjustSize()
tugma11.clicked.connect(obj.funk_olti)
tugma11.setStyleSheet("color:black;background-color:white")

tugma12=QPushButton("+",widget)
tugma12.setGeometry(240,210,50,50)
tugma12.setFont(QFont("Times",10))
tugma12.clicked.connect(obj.funk_qushish)

tugma13=QPushButton("1",widget)
tugma13.setGeometry(10,270,50,50)
tugma13.setFont(QFont("Times",10))
def bos():
    bir.setText("1")
    bir.adjustSize()
tugma13.clicked.connect(obj.funk_bir)
tugma13.setStyleSheet("color:black;background-color:white")

tugma14=QPushButton("2",widget)
tugma14.setGeometry(80,270,50,50)
tugma14.setFont(QFont("Times",10))
def bos():
    bir.setText("2")
    bir.adjustSize()
tugma14.clicked.connect(obj.funk_ikki)
tugma14.setStyleSheet("color:black;background-color:white")

tugma15=QPushButton("3",widget)
tugma15.setGeometry(150,270,50,50)
tugma15.setFont(QFont("Times",10))
def bos():
    bir.setText("3")
    bir.adjustSize()
tugma15.clicked.connect(obj.funk_uch)
tugma15.setStyleSheet("color:black;background-color:white")

tugma16=QPushButton("-",widget)
tugma16.setGeometry(240,270,50,50)
tugma16.setFont(QFont("Times",10))
tugma16.clicked.connect(obj.funk_ayirish)

tugma17=QPushButton("+/-",widget)
tugma17.setGeometry(10,330,50,50)
tugma17.setFont(QFont("Times",10))
tugma17.clicked.connect(obj.funk_pl_mn)

tugma18=QPushButton("0",widget)
tugma18.setGeometry(80,330,50,50)
tugma18.setFont(QFont("Times",10))
def bos():
    bir.setText("0")
    bir.adjustSize()
tugma18.clicked.connect(obj.funk_nol)
tugma18.setStyleSheet("color:black;background-color:white")

tugma19=QPushButton(".",widget)
tugma19.setGeometry(150,330,50,50)
tugma19.setFont(QFont("Times",10))
tugma19.clicked.connect(obj.funk_vergul)

tugma20=QPushButton("=",widget)
tugma20.setGeometry(240,330,50,50)
tugma20.setFont(QFont("Times",10))
tugma20.clicked.connect(obj.funk_teng)



widget.show()
app.exec_()