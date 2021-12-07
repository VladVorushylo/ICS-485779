import matplotlib.pyplot as plt

potato_price = [38.33, 40.00, 40.00]
cabbage_price = [36.67, 40.00, 40.00]
onion_price = [55.00, 51.67, 55.00]
time = ['02.11.2016', '14.11.2016', '22.11.2016']

plt.plot(time,potato_price,label = 'Картопля')
plt.plot(time,cabbage_price,label = 'Капуста')
plt.plot(time,onion_price,label = 'Цибуля')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.legend()
plt.title('Ринкові ціни')
plt.grid(True)

def showplot():
    plt.show()
