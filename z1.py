import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets

# Создаем окно приложения
app = QtWidgets.QApplication([])
# Создаем окно для графиков
win = pg.GraphicsLayoutWidget(show=True, title="Синус и Косинус")
win.resize(800, 600)
# Добавляем первый график (синус)
plot_sin = win.addPlot(title="График Синуса")
x = np.linspace(0, 2 * np.pi, 50)
y_sin = np.sin(x)
plot_sin.plot(x, y_sin, pen='r')
# Добавляем второй график (косинус)
win.nextRow() # Переходим на следующую строку для следующего графика
plot_cos = win.addPlot(title="График Косинуса")
y_cos = np.cos(x)
plot_cos.plot(x, y_cos, pen='b')
# Запускаем приложение
app.exec()