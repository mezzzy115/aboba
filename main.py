from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt
from random import randint
import sys

class aboba(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.clic)
        self.circles = []

    def clic(self):

        a = randint(20, 100)
        x = randint(0, 600)
        y = randint(0, 400)
        self.circles.append((x, y, a))
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor("yellow"))

        for x, y, a in self.circles:
            painter.drawEllipse(x, y, a, a)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = aboba()
    window.show()
    sys.exit(app.exec())
