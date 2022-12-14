import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QMessageBox

def onClick():
    QMessageBox.about(None, "О программе", "Простейший пример графического приложения")
                                                     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # label = QLabel("Hello World", alignment=Qt.AlignCenter)
    # label.show()
    mainwindow = QMainWindow()
    pushbutton = QPushButton(text="Пуск", parent=mainwindow)
    pushbutton.clicked.connect(onClick)
    pushbutton.setGeometry(20, 20, 50, 20)
    mainwindow.show()
    sys.exit(app.exec_())