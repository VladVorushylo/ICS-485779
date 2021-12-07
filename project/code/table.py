from prettytable import PrettyTable
from data import dt

x = PrettyTable()

x.field_names = ['Найменування ринку', 'Дата', 'Картопля',
                'Капуста', 'Цибуля', 'Середня ціна']

for i in range (0, len(dt)):
    x.add_rows(
        [
            dt[i]
        ]
    )

def opentabble():
    print('\nАналіз середніх ринкових цін на основні продукти споживчого кошика')
    print(x)
