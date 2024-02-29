def ex6_1():
    countries_and_capitals = {
        "Россия": "Москва",
        "Франция": "Париж",
        "Германия": "Берлин",
        "Италия": "Рим",
        "Япония": "Токио",
        "США": "Вашингтон",
        "Китай": "Пекин",
        "Великобритания": "Лондон",
        "Индия": "Нью-Дели",
        "Бразилия": "Бразилиа"
    }

    print('\nВсе пары ключ-значение:')
    for key, value in countries_and_capitals.items():
        print(f'{key}: {value}', end='; ')
    print('\n\nСтолица для определенной страны:\n', countries_and_capitals['Франция'])
    print('\nОтсортированный список:')
    for key in sorted(countries_and_capitals):
        print(key, end='; ')


def ex6_2():
    def get_key_by_value(dictionary, search_value):
        for key, value in dictionary.items():
            if search_value.lower() in value.lower():
                return key
        return 0

    erudite = {
        1: 'АВЕИНОРСТ',
        2: 'ДКЛМПУ',
        3: 'БГЁЯ',
        4: 'ЙЫ',
        5: 'ЖЗХЦЧ',
        8: 'ШЭЮ',
        10: 'ФЩЪ'
    }
    check_stop = 'y'
    while 'n' not in check_stop:
        word = input('Введите ваше слово: ')
        res = sum(get_key_by_value(erudite, i) for i in word.upper())
        print(f'Стоимость введенного слова: {res}')
        check_stop = input('Желаете продолжить (y/n)? ').strip().lower()
        if check_stop == 'n':
            break


def ex6_3():
    students_languages = {
        "Иванов": {"английский", "французский", "немецкий"},
        "Петров": {"английский", "испанский", "китайский"},
        "Сидоров": {"французский", "китайский", "японский"},
        "Козлов": {"английский", "китайский", "русский"},
        "Никитин": {"немецкий", "китайский", "русский"},
        "Смирнов": {"испанский", "русский", "французский"},
        "Кузнецов": {"английский", "немецкий", "корейский"},
        "Васильев": {"английский", "русский", "итальянский"},
        "Попов": {"испанский", "португальский", "китайский"},
        "Морозов": {"норвежский", "финский", "датский"}
    }
    all_languages = set()

    for languages in students_languages.values():
        all_languages.update(languages)
    print('Количество языков которых знают студенты:', len(all_languages))
    print('Список языков:', end=' ')
    print(*all_languages, sep=', ')
    print("Список студентов, которые знают китайский язык:", end=' ')
    for key, value in students_languages.items():
        if 'китайский' in value:
            print(key, end=', ')


ex = int(input('Введите номер задания: '))
match ex:
    case 1:
        # first
        ex6_1()
    case 2:
        # second
        ex6_2()
    case 3:
        # third
        ex6_3()
