from contracts.sql import *
import json

print('Базовый интерфейс для работы с данными из документов.')
print('Возвращает место поставки по номеру заказа, и заказы по месту поставки.')

while True:
    input_ = input('Введите город или номер заказа: ')
    try:
        input_order = int(input_)
        print(search(order=str(input_order)))
    except:
        print(search(city=input_))