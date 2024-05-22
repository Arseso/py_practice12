import pandas as pd
import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets

# Загрузка данных из файла
data = pd.read_csv('data/trees.csv')

height = data['Height'].values
girth = data['Girth'].values

# Создаем окно приложения
app = QtWidgets.QApplication([])

# Создаем окно для графиков
win = pg.GraphicsLayoutWidget(show=True, title="Данные о деревьях")
win.resize(800, 600)

# Добавляем график точечной диаграммы
scatter_plot = win.addPlot(title="Высота / Обхват")
scatter_plot.plot(height, girth, pen=None, symbol='o')

# Запускаем приложение
app.exec()