import json
from collections import defaultdict


def ex10_1():
    with open('products.json') as f:
        data = json.load(f)

    product_list = data['products']
    for product in product_list:
        name = product['name']
        price = product['price']
        available = 'В наличии' if product['available'] else 'Нет в наличии!'
        weight = product['weight']

        print(f'Название: {name}\n'
              f'Цена: {price}\n'
              f'Вес: {weight}\n'
              f'{available}\n')


def ex10_2():
    with open('products.json', 'r') as f:
        data = json.load(f)

    name = input('Введите название: ')
    price = input('Введите цену: ')
    available = input('Введите "В наличии" или "Нет в наличии!": ')
    weight = input('Введите вес: ')
    products = [
        {
            "name": name,
            "price": price,
            "available": available,
            "weight": weight
        }
    ]
    data['products'].extend(products)
    with open('products.json', 'w') as f:
        json.dump(data, f, indent=4)
    ex10_1()


def ex10_3():
    f = list(open('en-ru.txt'))
    dict_ru_en = defaultdict(list)
    for line in f:
        en = line[:line.index('-')].strip()
        ru = line[line.index('-') + 1:].strip()
        if ',' in ru:
            words = ru.split(',')
            dict_ru_en[words[0].strip()].append(en)
            dict_ru_en[words[1].strip()].append(en)
        else:
            dict_ru_en[ru].append(en)

    f_w = open('ru-en.txt', 'w')
    for ru, en in sorted(dict_ru_en.items()):
        f_w.write(ru + ' - ' + ', '.join(en) + '\n  ')


ex = int(input('Введите номер задания: '))
match ex:
    case 1:
        # first
        ex10_1()
    case 2:
        # second
        ex10_2()
    case 3:
        # third
        ex10_3()
    case _:
        print('такого задания нет!')
