import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('src/movs.ui', self)
        self.findb = self.findChild(QPushButton, "find")
        self.findb2 = self.findChild(QPushButton, "find_2")
        self.finder = self.findChild(QComboBox, "finder")
        self.filmlist = self.findChild(QTableWidget, "filmfinder")
        self.genres = []
        self.con = sqlite3.connect("src/films.db")
        self.cur = self.con.cursor()
        result = self.cur.execute("""SELECT * FROM genres""").fetchall()
        for res in result:
            self.genres.append(res[1])
            print(res[1])

        self.con.close()
        for elem in self.genres:
            self.finder.addItem(elem)

        self.findb.clicked.connect(self.butt)
        self.findb2.clicked.connect(self.butt2)

    def butt(self):
        text = self.finder.currentText()
        id = self.genres.index(text)
        self.con = sqlite3.connect("src/films.db")
        self.cur = self.con.cursor()
        res = self.cur.execute("""SELECT title, genre, year, duration FROM Films WHERE (genre = ?)""",
                               (id+1,)).fetchall()
        self.filmlist.setRowCount(len(res))
        self.filmlist.setColumnCount(4)
        for i in range(1, len(res)):
            for j in range(4):
                try:
                    self.filmlist.setItem(i, j, QTableWidgetItem(str(res[i][j])))
                except:
                    print("pipiska")
                    pass
        self.con.close()

    def butt2(self):
        self.con = sqlite3.connect("src/films.db")
        self.cur = self.con.cursor()
        res = self.cur.execute("""SELECT title, genre, year, duration FROM Films WHERE (genre = 6)""").fetchall()
        self.filmlist.setRowCount(len(res))
        self.filmlist.setColumnCount(4)
        for i in range(1, len(res)):
            for j in range(4):
                try:
                    self.filmlist.setItem(i, j, QTableWidgetItem(str(res[i][j])))
                except:
                    print("pipiska")
                    pass
        self.con.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWindow()
    ui.show()
    sys.exit(app.exec_())
