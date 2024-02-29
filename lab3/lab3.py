import random


def ex3_1():
    n = int(input('Введите допустимое количество слов: '))
    lst = []
    for _ in range(n):
        word = input('Введите слово: ')
        if word.isalpha():
            lst.append(word)
    print(*lst)


def ex3_2():
    lst = []
    word = input('Введите слово или слов stop, если хотите завершится: ')
    while 'stop' not in word:
        lst.append(word)
        word = input('Введите слово или слов stop, если хотите завершится: ')
    print(*lst)


def ex3_3():
    word = input('Введите слово или слов stop, если хотите завершится: ')
    while 'stop' not in word:
        if 'ф' in word or 'Ф' in word:
            print('Ого! Это редкое слово!')
        else:
            print('Эх, это не очень редкое слово...')
        word = input('Введите слово или слов stop, если хотите завершится: ')


def ex3_4():
    res = 0
    err = 0
    while err != 3:
        a = random.randrange(101)
        b = random.randrange(101)
        ans = int(input(f'{a} + {b} = '))
        if (a + b) == ans:
            print('Правильно!')
            res += 1
        else:
            print('Ответ неправильный')
            err += 1
            print(f'Осталось возможных допустипых ошибок: {3 - err}')

    print(f'Игра окончена. \n'
          f'Правильных ответов: {res}')


ex = int(input('Введите номер задания: '))

match ex:
    case 1:
        # first
        ex3_1()
    case 2:
        # second
        ex3_2()
    case 3:
        # third
        ex3_3()
    case 4:
        # fourth
        ex3_4()
