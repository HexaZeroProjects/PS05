import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.hist(data, bins=30, alpha=0.7, color='blue')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()


# Генерация двух наборов случайных данных
num_points = 100
x_data = np.random.rand(num_points)
y_data = np.random.rand(num_points)

# Построение диаграммы рассеяния
plt.scatter(x_data, y_data, alpha=0.7, color='green')
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()



# Загрузка данных
file_path = 'spiders/results_20241105200834.csv'
data = pd.read_csv(file_path)

# Очистка столбца price от пробелов
data['price'] = data['price'].str.replace(' ', '', regex=True)

# Преобразование столбца price в числовой тип данных
data['price'] = pd.to_numeric(data['price'], errors='coerce')

# Вычисление средней цены
average_price = data['price'].mean()
print(f"Средняя цена на диваны: {average_price:.2f} руб.")

# Построение гистограммы цен
plt.hist(data['price'].dropna(), bins=30, alpha=0.7, color='purple')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (руб)')
plt.ylabel('Частота')
plt.show()

