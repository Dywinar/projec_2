import matplotlib.pyplot as plt
import pandas as pd
import random
data = pd.read_csv('/content/Housing.csv')
plt.figure(figsize=(10,10))
data_with_airconditioning =  data[data['airconditioning']=='yes']
data_wihtout_airconditioning =  data[data['airconditioning']=='no']
plt.hist([data_with_airconditioning['price'], data_wihtout_airconditioning['price']], bins=50, alpha=0.5, color=['blue', 'red'], label=['Распределения цены (дома  с наличием кондиционирования', 'Распределения цены (дома  без кондиционирования' ])
plt.title('Гистограмма')
plt.legend()
plt.show()
