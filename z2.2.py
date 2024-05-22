import pandas as pd
import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets

# Загрузка данных из файла
data = pd.read_csv('data/hurricanes.csv')

# Фильтрация данных за 2007 год

# Подсчет количества ураганов по месяцам
hurricanes_per_month = data['2007']

# Создаем окно приложения
app = QtWidgets.QApplication([])

# Создаем окно для графиков
win = pg.GraphicsLayoutWidget(show=True, title="Ураганы 2007 года по месяцам")
win.resize(800, 600)

# Добавляем столбчатую диаграмму
bar_plot = win.addPlot(title="Ураганы 2007 года по месяцам")
months = hurricanes_per_month.index.values
counts = hurricanes_per_month.values
bg = pg.BarGraphItem(x=months, height=counts, width=0.6, brush='r')
bar_plot.addItem(bg)

# Запускаем приложение
app.exec()