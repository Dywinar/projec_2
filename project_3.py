import matplotlib.pyplot as plt
import pandas as pd
import random
data = pd.read_csv('/content/Housing.csv')
fig, axes = plt.subplots(4, figsize=(20,22))
nazv = ['guestroom', 'basement','hotwaterheating', 'prefarea']
nazv2 = ['гостевой комнаты', 'подвала', 'обогрева с помощью горячей воды', 'предбанника']
color_1 = ['red', 'blue', 'orange', 'green']
color_2 = ['purple', 'yellow', 'black', 'pink', 'brown']
for i  in range(4):
  data_with_something = data[data[nazv[i]] ==  'yes']
  axes[i].scatter(data_with_something['price'], data_with_something['area'], alpha=0.5, c = random.choice(color_1), label=f'Наличие {nazv2[i]}: yes')
for i  in range(4):
  data_with_something = data[data[nazv[i]] ==  'no']
  axes[i].scatter(data_with_something['price'], data_with_something['area'], alpha=0.5, c= random.choice(color_2), label=f'Наличие {nazv2[i]}: no')
  axes[i].set_ylabel('Цена')
  axes[i].set_xlabel('Площадь')
  axes[i].legend()
  axes[i].set_title(f'График наличия {nazv2[i]}')
  axes[i].grid()
plt.show()
