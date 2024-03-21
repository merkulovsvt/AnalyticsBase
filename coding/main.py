import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Предположим, у вас есть данные с id и соответствующими числами
# Ваш список id (в примере создается случайным образом)
id_list = np.arange(1, 1001)
# Ваши числа (замените их на ваши фактические данные)
data_list = np.random.rand(1000)

# Создайте DataFrame из ваших данных
import pandas as pd
df = pd.DataFrame({'id': id_list, 'data': data_list})

# Настройте параметры Seaborn
sns.set(style="whitegrid")

# Создайте график
plt.figure(figsize=(10, 6))
sns.lineplot(x='id', y='data', data=df)

# Настройте метки на оси x через каждые 100 значений
plt.xticks(np.arange(1, 1001, 100))

# Добавьте заголовок и метки осей
plt.title('График данных с метками id через каждые 100 значений')
plt.xlabel('id')
plt.ylabel('Ваши числа')

# Покажите график
plt.show()