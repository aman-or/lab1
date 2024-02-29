import random


def check_password(pas):
    check = 0
    for i in pas:
        if i.isdigit():
            check += 1
    if len(pas) >= 12 and check > 1:
        print('Ваш пароль правильный!')
    else:
        print('Некоректный пароль')


def check_place(place):
    if place in range(1, 55):
        print('Ваше место верхнее' if place % 2 == 0 else 'Ваше место нижнее')
    else:
        print('Вашего места не существует')


def check_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Год високосный')
    else:
        print('Год невисокосный')


def check_color(a, b):
    print(f'наши цвета {a} и {b}')
    if a == b:
        print(a)
    elif a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
        print('Ваш цвет: фиолетовый')
    elif a == 'красный ' and b == 'желтый' or a == 'желтый' and b == 'красный':
        print('Ваш цвет: оранжевый')
    elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
        print('Ваш цвет: синий')


ex = int(input('Введите номер задания: '))

match ex:
    case 1:
        # first
        password = input('Введите пароль, пароль должен быть не менее 12 символов и содержать цифры: ')
        check_password(password)
    case 2:
        # second
        place = int(input('Введите ваше место от 1 до 54: '))
        check_place(place)
    case 3:
        # third
        year = int(input('Введите год: '))
        check_year(year)
    case 4:
        # fourth
        lst = ['красный', 'синий', 'желтый']
        first = random.choice(lst)
        second = random.choice(lst)
        check_color(first, second)
