from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon("images/hellcatredeye.png"))
        #self.setFixedWidth(700)
        #self.setFixedHeight(400)

        self.setStyleSheet('background-color:cyan')
        self.setWindowOpacity(0.5)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())