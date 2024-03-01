from PIL import Image, ImageDraw, ImageFont


def ex8_1():
    image = Image.open('edit_images/raw.png')
    # image.show()
    width, height = image.size
    print(width, 'x', height)
    left = 10
    top = 180
    right = width - 470
    bottom = height - 10
    image.crop((left, top, right, bottom)).save('edit_images/crop_image.png')


def ex8_2():
    holidays = {
        'Праздник октября': Image.open('Holidays/1.jpg'),
        'Первое мая': Image.open('Holidays/2.jpg'),
        'День космонавтики': Image.open('Holidays/3.jpg'),
        'Новый год': Image.open('Holidays/4.jpg'),
        'Восьмое марта': Image.open('Holidays/5.jpeg')
    }
    check_stop = 'y'
    while 'n' not in check_stop:
        name_holiday = input(
            'К какому празднику вам нужна отрытка?: '
            '(Праздник октября, Первое мая, День космонавтики, Новый год, Восьмое марта): ')
        if name_holiday in holidays.keys():
            holidays[name_holiday].show()
        else:
            print("Извините, открытка для этого праздника не найдена.")

        check_stop = input('Желаете продолжить (y/n)? ')


def ex8_3():
    image = Image.open('edit_images/crop_image.png')
    text = input('Напишите имя пользователя, которого вы хотите поздравить: ')
    font = ImageFont.truetype("arial_bolditalicmt.ttf", 46)
    drawer = ImageDraw.Draw(image)
    drawer.text((50, image.width / 1.5 + 130), f'{text}, поздравляю!', fill='white', font=font)
    image.save('edit_images/img_with_name.png')


ex = int(input('Введите номер задания: '))
match ex:
    case 1:
        # first
        ex8_1()
    case 2:
        # second
        ex8_2()
    case 3:
        # third
        ex8_3()
