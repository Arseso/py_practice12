import pandas as pd
import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets

# Загрузка данных из файла
data = pd.read_csv('data/hurricanes.csv')

hurricanes_per_year = pd.DataFrame({
    "Year": data.columns.values[2:],
    "Hurricanes": data.sum(axis=0)[2:],
})

# Convert Year to integers and Hurricanes to floats
hurricanes_per_year["Year"] = hurricanes_per_year["Year"].astype(int)
hurricanes_per_year["Hurricanes"] = hurricanes_per_year["Hurricanes"].astype(float)

# Создаем окно приложения
app = QtWidgets.QApplication([])

# Создаем окно для графиков
win = pg.GraphicsLayoutWidget(show=True, title="Ураганы по годам")
win.resize(800, 600)

# Добавляем столбчатую диаграмму
bar_plot_years = win.addPlot(title="Ураганы по годам")
years = hurricanes_per_year["Year"].values
year_counts = hurricanes_per_year["Hurricanes"].values
bg_years = pg.BarGraphItem(x=years, height=year_counts, width=0.6, brush='b')
bar_plot_years.addItem(bg_years)

# Запускаем приложение
app.exec()

