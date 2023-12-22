import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('/content/Housing.csv')
#print(data['parking'].unique()) посмотрел всего 4 уникальных значений парковки 
kol_vo_park = data['parking'].unique()
plt.figure(figsize=(11,5))
color = ['blue', 'red', 'green', 'yellow']
for i in range(4):
  data_parkin = data[kol_vo_park[i] == data['parking']]
  plt.scatter(data_parkin['price'], data_parkin['area'], color=color[i], alpha=0.5, label=f'Кол-во пакровок: {kol_vo_park[i]}')
plt.ylabel('Цена')
plt.xlabel('Площадь')
plt.legend()
plt.show()
