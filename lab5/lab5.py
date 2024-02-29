from random import randint, choice


def ex5_1():
    check_stop = 'y'
    while 'n' not in check_stop:
        lst = [randint(1, 11) for _ in range(5)]
        n = int(input('Введите число: '))
        if n in lst:
            print(f'Список: {lst}\n'
                  f'Ваше число {n}\n'
                  f'Поздравляю, Вы угадали число!')
            check_stop = input('Желаете продолжить (y/n)? ')
        else:
            print(f'Список: {lst}\n'
                  f'Ваше число {n}\n'
                  f'Нет такого числа!')
            check_stop = input('Желаете продолжить (y/n)? ')


def ex5_2():
    check_stop = 'y'
    while 'n' not in check_stop:
        lst = [randint(1, 11) for _ in range(5)]
        check_return = set()
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j]:
                    check_return.add(lst[i])
        if len(check_return) != 0:
            print(f'Наш список: {lst}\n'
                  f'Повторяющиеся элементы: {check_return}')
            check_stop = input('Желаете продолжить (y/n)? ')
        else:
            print(f'Наш список: {lst}\n'
                  f'Нет повторяющихся элементов!')
            check_stop = input('Желаете продолжить (y/n)? ')


def ex5_3():
    weak = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
    check_stop = 'y'
    while 'n' not in check_stop:
        n = int(input('Cколько выходных на неделе вы хотите: '))
        print('Ваши выходные дни: ', *weak[-1: -n - 1: -1])
        print('Ваши рабочие дни: ', *weak[0: -n:])
        check_stop = input('Желаете продолжить (y/n)? ')


def ex5_4():
    # Первый список
    group1 = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Михайлов", "Федоров", "Смирнов", "Алексеев", "Козлов",
              "Николаев"]

    # Второй список
    group2 = ["Иванов", "Васильев", "Козлов", "Попов", "Соколов", "Лебедев", "Ковалев", "Морозов", "Павлов", "Никитин"]
    check_stop = 'y'
    while 'n' not in check_stop:
        team = tuple(choice(group1 + group2) for _ in range(5))
        print('Группа1: ', group1)
        print('Группа2: ', group2)
        print('Новая команда: ', team)
        print('Длина: ', len(team))
        print('Группа по алфавиту:', sorted(team))
        search_ivanov = team.count('Иванов')
        print(f'Фамилия Иванов встречается в группе: {search_ivanov}' if search_ivanov != 0 else 'Фамилии Иванов нет!')
        check_stop = input('Желаете продолжить (y/n)? ')


ex = int(input('Введите номер задания: '))
match ex:
    case 1:
        # first
        ex5_1()
    case 2:
        # second
        ex5_2()
    case 3:
        # third
        ex5_3()
    case 4:
        # fourth
        ex5_4()
