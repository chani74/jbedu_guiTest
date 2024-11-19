# pip install PyQt5
from PyQt5.QtWidgets import QWidget
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

class MyWindow(QWidget): # QWidget 클래스를 상속 받는 자식 클래스 선언
    def __init__(self): #생성장(초기화자) 선언
        super().__init__()  #부모 클래스의 생성장 호출
        self.initUI()   #initUI() 함수를 객체가 생성될 때 자동으로 호출

    def initUI(self):
        self.setWindowTitle("나의 파이썬 프로그램") # 윈도우 타이틀( 프로그램 제목 )
        self.setWindowIcon(QIcon("google.png"))
        self.resize(300,500) # 내가 만들 윈도우의 창 크기 ( 가로, 세로 )
        self.show()     # 윈도우 창을 화면에 표시함


app = QApplication(sys.argv)
win = MyWindow()
sys.exit(app.exec_())
