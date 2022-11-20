from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
import sys
class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.real_password=123456
        self.real_name="zafer"
        while True:
            self.password=int(input("Password: "))
            self.name=input("name: ")
            if (self.password==self.real_password) and (self.name==self.real_name) :
                self.initUI()
                break
    def initUI(self):
        self.setGeometry(10,10,600,400)
        self.setWindowTitle("password check")
        self.LabelMerhaba=QLabel("",self)
        self.LabelMerhaba.setGeometry(200,100,200,200)
        self.LabelMerhaba.setText(f"Hello {self.name}. Welcome")
        self.show()


            


app=QApplication(sys.argv)

win=Win()
sys.exit(app.exec())