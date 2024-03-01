from PIL import Image, ImageFilter
import os


def ex7_1():
    image = Image.open('cat.jpg')
    image.show()
    width, height = image.size
    image_format = image.format
    color_mode = image.mode
    print("Размер изображения:", width, "x", height)
    print("Формат изображения:", image_format)
    print("Цветовая модель изображения:", color_mode)


def ex7_2():
    image = Image.open('cat.jpg')
    width, height = image.size
    cropped_img = image.resize((width // 3, height // 3))
    cropped_img.transpose(Image.FLIP_TOP_BOTTOM).save('flip_t_p.jpg')
    cropped_img.transpose(Image.FLIP_LEFT_RIGHT).save('flip_l_r.jpg')


def ex7_3():
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

    # Сохраняем каждое изображение в new_images папку
    for i, image in enumerate(image_list):
        output_path = os.path.join('new_images', f"{i + 1}.jpg")
        image.filter(ImageFilter.FIND_EDGES).save(output_path)


def ex7_4():
    folder_path = 'new_images'
    images_list = []
    files = os.listdir(folder_path)
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg'))]
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        img = Image.open(image_path)
        images_list.append(img)

    watermark = Image.open('watermark_images/mark.png')
    watermark_width, watermark_height = watermark.size

    for i, image in enumerate(images_list):
        image_width, image_height = image.size
        position = (image_width - watermark_width, image_height - watermark_height)
        output_path = os.path.join('watermark_images', f"{i + 1}.jpg")
        image.paste(watermark, position)
        image.save(output_path)


ex = int(input('Введите номер задания: '))
match ex:
    case 1:
        # first
        ex7_1()
    case 2:
        # second
        ex7_2()
    case 3:
        # third
        ex7_3()
    case 4:
        # third
        ex7_4()
