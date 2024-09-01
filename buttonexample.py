from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QPushButton")
        self.setWindowIcon(QIcon("images/hellcatredeye.png"))

        self.create_button()
    def create_button(self):
        btn = QPushButton("Click", self)
        btn.setGeometry(100, 100, 130,130)
        btn.setFont(QFont("Times", 14, QFont.Weight.Bold))
        btn.setIcon(QIcon("images/hellcatredeye.png"))
        btn.setIconSize(QSize(36,36))

        #popup menu
        menu = QMenu()
        menu.setFont(QFont("Times", 14, QFont.Weight.Bold))
        menu.setStyleSheet('background-color: cyan')
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())