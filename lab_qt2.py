import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel



app = QApplication() # создать объект "приложение" (но ещё не запустить и не отобразить)
mainwindow = QMainWindow()
checkbox = QCheckBox(parent=mainwindow, text="Это пример QCheckbox")
checkbox.setGeometry(50, 50, 200, 20)
label = QLabel(parent=mainwindow, text="Здесь будет выведен результат 5**2 + 7**2")

def onChecked():
    # эта функция (коллбек) будет срабатывать при нажатии
    label.setText(f"Результат расчёта = {5**2 + 7**2}")
    return
checkbox.clicked.connect(onChecked)

label.setGeometry(50, 70, 300, 20)
mainwindow.show()
app.exec() # бесконечный цикл, во время которого приложение висит в памяти и ждёт команд пользователя