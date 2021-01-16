import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel



class addcoffe(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.save)



    def save(self):
        text = self.lineEdit.text().split(",")
        con = sqlite3.connect("coffe.sqlite")
        cur = con.cursor()
        print(text)
        cur.execute(f"""INSERT INTO coffee(name, roasting, condition, description, cost, volume) VALUES('{text[0]}', '{text[1]}', '{text[2]}', '{text[3]}','{int(text[4])}','{int(text[5])}')""")
        con.commit()
        self.hide()
