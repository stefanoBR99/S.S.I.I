import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QWidget, QVBoxLayout,QLabel,QComboBox
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui

class Window1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recomendaciones de peliculas")
        self.setGeometry(100, 100, 600, 400)
        self.button1 = QPushButton("Recomendaciones por pelicula", self)
        self.button1.clicked.connect(self.ventana2)
        self.button2 = QPushButton("Recomendaciones por id de usuario", self)
        self.button2.clicked.connect(self.ventana3)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

    def ventana2(self):
        self.window2 = Window2()
        self.window2.show()

    def ventana3(self):
        self.window3 = Window3()
        self.window3.show()

class Window2(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recomendaciones de nombre de pelicula")
        self.setGeometry(100, 100, 600, 400)
        self.label1 = QtWidgets.QLabel("Nombre de la pelicula")
        self.combo1 = QtWidgets.QComboBox()
        self.combo1.addItems(["Opción 1", "Opción 2", "Opción 3"])
        self.label2 = QtWidgets.QLabel("Numero de la pelicula")
        self.combo2 = QtWidgets.QComboBox()
        for i in range(1, 11):
            self.combo2.addItem(str(i))
        
        
        self.listView1 = QtWidgets.QListView()
        self.listView1.setModel(QtGui.QStandardItemModel(self.listView1))
        self.add_button = QtWidgets.QPushButton("Siguiente", self)
        self.add_button.clicked.connect(self.siguiente)
        self.back_button = QPushButton("Atras", self)
        self.back_button.clicked.connect(self.atras)
        self.selection_list = []

        layout = QVBoxLayout(self)
        layout.addWidget(self.label1)
        layout.addWidget(self.combo1)
        layout.addWidget(self.label2)
        layout.addWidget(self.combo2)
        layout.addWidget(self.add_button)
        layout.addWidget(self.listView1)        
        layout.addWidget(self.back_button)

    def siguiente(self):
        self.selection_list.append(self.combobox.currentText())
        print(self.selection_list)

    def atras(self):
        self.close()
        self.main = Window1()
        self.main.show()
    

    

class Window3(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recomendaciones por Id de Usuario")
        self.setGeometry(100, 100, 600, 400)
        self.label3 = QtWidgets.QLabel("Id del usuario")
        self.combo3 = QtWidgets.QComboBox()
        self.combo3.addItems(["Opción 4", "Opción 5", "Opción 6"])
        self.label4 = QtWidgets.QLabel("Numero de la pelicula")
        self.combo4 = QtWidgets.QComboBox()
        for i in range(1, 11):
            self.combo4.addItem(str(i))
        self.add_button = QPushButton("Siguiente", self)
        self.add_button.clicked.connect(self.siguiente)

        self.listView2 = QtWidgets.QListView()
        self.listView2.setModel(QtGui.QStandardItemModel(self.listView2))
        self.back_button = QPushButton("Atras", self)
        self.back_button.clicked.connect(self.atras)
        self.selection_list = []

        layout = QVBoxLayout(self)
        layout.addWidget(self.label3)
        layout.addWidget(self.combo3)
        layout.addWidget(self.label4)
        layout.addWidget(self.combo4)
        layout.addWidget(self.add_button)
        layout.addWidget(self.listView2)
        layout.addWidget(self.back_button)

    def siguiente(self):
        self.selection_list.append(self.combobox.currentText())
        print(self.selection_list)

    def atras(self):
        self.close()
        self.main = Window1()
        self.main.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window1 = Window1()
    window1.show()
    sys.exit(app.exec_())
