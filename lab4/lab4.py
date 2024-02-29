def ex4_1():
    check_stop = 'y'
    while 'n' not in check_stop:
        n = int(input('Введите число: '))
        if n % 3 == 0:
            print(f'{n // 3}  - число, получившееся после деления на 3')
            check_stop = input('Желате продилжить (y/n)? ')
        else:
            print(f'{n} - не делится на 3')
            check_stop = input('Желате продилжить (y/n)? ')


def ex4_2():
    check_stop = 'y'
    while 'n' not in check_stop:
        try:
            n = int(input('Введите число: '))
            p = 100 / n
        except ValueError:
            print('Это не число. Выходим.')
            check_stop = input('Желате продилжить (y/n)? ')
        except ZeroDivisionError:
            print('Нельзя делить на ноль. Выходим.')
            check_stop = input('Желате продилжить (y/n)? ')
        else:
            print(f'Ваше число после деления: {p}')
            check_stop = input('Желате продилжить (y/n)? ')


def ex4_3():
    check_stop = 'y'
    while 'n' not in check_stop:
        magic_data = [int(x) for x in input('Введите дату в формате DD.MM.YYYY: ').split('.') if x.strip()]
        print(magic_data[0] * magic_data[1] == magic_data[2] % 100)
        check_stop = input('Желате продилжить (y/n)? ')


def ex4_4():
    a, b = [], []
    check_stop = 'y'
    while 'n' not in check_stop:
        number = input('введите число: ')
        if len(number) % 2 == 0:
            a.extend(number[: len(number) // 2])
            b.extend(number[len(number) // 2:])
            print('У вас счастливый билет' if sum([int(i) for i in a]) ==
                                              sum([int(i) for i in b]) else 'У вас несчастливый билет')
            check_stop = input('Желате продилжить (y/n)? ')
        else:
            print('Число не подходит по количеству цифр')
            check_stop = input('Желате продилжить (y/n)? ')


ex = int(input('Введите номер задания: '))
match ex:
    case 1:
        # first
        ex4_1()
    case 2:
        # second
        ex4_2()
    case 3:
        # third
        ex4_3()
    case 4:
        # fourth
        ex4_4()
