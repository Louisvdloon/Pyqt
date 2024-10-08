from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QLineEdit")
        self.setWindowIcon(QIcon("images/hellcatredeye.png"))

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Sanserif", 15))
        #line_edit.setText("Default Text")
        #line_edit.setPlaceholderText("Username")
        #line_edit.setEnabled(False)
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())