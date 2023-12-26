import matplotlib.pyplot as plt
import pandas as pd
import random
data = pd.read_csv('/content/Housing.csv')
plt.figure(figsize=(10,10))
data_with_airconditioning =  data[data['airconditioning']=='yes']
data_wihtout_airconditioning =  data[data['airconditioning']=='no']
#plt.hist([data_with_airconditioning['price'], data_wihtout_airconditioning['price']], bins=50, alpha=0.5, color=['blue', 'red'], label=['Распределения цены (дома  с наличием кондиционирования)', 'Распределения цены (дома  без кондиционирования)' ]) #вот как бы 2 способ но думаю он не сильно коректен, почему я сделал еще 2 способ, ну так как цвета в 1 способе совмещаются, что меня очень смущает хотя все равно можно просматривать информацию, так что вроде 1 подходит, но на всякий вот 2 способ (но на счет него не очень уверен)
plt.hist(data_with_airconditioning['price'],100, alpha=0.5, color='red', label='Распределения цены (дома  с наличием кондиционирования)')
plt.hist(data_wihtout_airconditioning['price'],100, alpha=0.5, color='blue',label='Распределения цены (дома  без кондиционирования)' )
plt.ylabel('Цена')
plt.title('Гистограмма')
plt.legend()
plt.show()
