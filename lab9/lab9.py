from PIL import Image, ImageFilter
import os
import csv


def ex9_1():
    folder_path = 'old_images'
    image_list = []
    files = os.listdir(folder_path)

    # Фильтруем только файлы с изображениями (расширения .jpg)
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg'))]
    for image_file in image_files:
        # Формируем полный путь к изображению
        image_path = os.path.join(folder_path, image_file)

        # Открываем изображение
        image = Image.open(image_path)

        # Добавляем изображение в список
        image_list.append(image)

    # создаем папку
    folder_name = "new_images"
    if not os.path.exists(folder_name):
        os.mkdir(os.path.join('', 'new_images'))
        print(f"Папка '{folder_name}' создана успешно.")
    else:
        print(f"Папка '{folder_name}' уже существует.")

    # Сохраняем каждое изображение в new_images папку
    for i, image in enumerate(image_list):
        output_path = os.path.join('new_images', f"{i + 1}.jpg")
        image.filter(ImageFilter.FIND_EDGES).save(output_path)


def ex9_2():
    folder_path = 'old_images'
    image_list = []
    files = os.listdir(folder_path)

    # Фильтруем только файлы с изображениями (расширения .jpg, .png)
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png'))]
    for image_file in image_files:
        # Формируем полный путь к изображению
        image_path = os.path.join(folder_path, image_file)

        # Открываем изображение
        image = Image.open(image_path)

        # Добавляем изображение в список
        image_list.append(image)

    # создаем папку
    folder_name = "new_images"
    if not os.path.exists(folder_name):
        os.mkdir(os.path.join('', 'new_images'))
        print(f"Папка '{folder_name}' создана успешно.")
    else:
        print(f"Папка '{folder_name}' уже существует.")

    # Сохраняем каждое изображение в new_images папку
    for i, image in enumerate(image_list):
        output_path = os.path.join('new_images', f"{i + 1}.jpg")
        image.filter(ImageFilter.FIND_EDGES).save(output_path)


def ex9_3():
    with open('list_of_products.csv', 'r', newline='') as csvfile:
        list_of_products = list(csv.reader(csvfile))
        res = 0
        print('Нужно купить: ')
        for i in range(1, len(list_of_products)):
            print(f'{list_of_products[i][0]} - {list_of_products[i][1]} шт. за {list_of_products[i][2]} руб.')
            res += int(list_of_products[i][1]) * int(list_of_products[i][2])
        print('Итоговая сумма:', res)


ex = int(input('Введите номер задания: '))
match ex:
    case 1:
        # first
        ex9_1()
    case 2:
        # second
        ex9_2()
    case 3:
        # third
        ex9_3()
    case _:
        print('такого задания нет!')
