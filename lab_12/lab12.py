from tkinter import *


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating_points):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating_points = rating_points

    def describe_restaurant(self):
        if self.rating_points is None:
            print(f'Ресторан {self.restaurant_name} {self.cuisine_type} кухня.')
        else:
            print(f'Ресторан {self.restaurant_name} {self.cuisine_type} кухня. Рейтинг: {self.rating_points}')

    def open_restaurant(self):
        print(f'Ресторан {self.restaurant_name} открыт')

    def rating(self, rating_points):
        self.rating_points = rating_points
        print(f'Рейтинг ресторана {self.restaurant_name} обновлен: {rating_points}')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating_points, flavors: list, location, time):
        Restaurant.__init__(self, restaurant_name, cuisine_type, rating_points)
        self.flavors = flavors
        self.location = location
        self.time = time

    def print_flavors(self):
        print('Список сортов мороженого: ' + ', '.join(self.flavors))

    def print_location_and_time(self):
        print(f'Локация: {self.location}\n Время работы: {self.time}')

    def add_flavors(self):
        flavor = input('Введите сорт мороженного, которое хотите добавить: ')
        self.flavors.append(flavor)

    def del_flavors(self):
        flavor = input('Введите сорт мороженного, которое хотите удалить: ')
        del self.flavors[self.flavors.index(flavor)]

    def search_flavor(self):
        flavor = input('Введите сорт мороженного, которое хотите найти: ')
        print(f'{flavor} есть в наличии' if flavor in self.flavors else f'{flavor} нет в наличии')

    def stick_ice_cream(self, flavor):
        print(f'Мороженное на палочке: {flavor}')

    def soft_ice_cream(self, flavor, topping):
        print(f'Мягкое мороженное: {flavor} и топинг: {topping}')


if __name__ == "__main__":
    ex = int(input('Введите номер задания: '))
    match ex:
        case 1:
            # first
            ice_cream_restaurant = IceCreamStand('Cool Ice Creams', 'западная', 4.5,
                                                 ['пломбир', 'сливочное', 'молочное', 'крем-брюле', 'шербет', 'мягкое'],
                                                 None, None)
            ice_cream_restaurant.describe_restaurant()
            ice_cream_restaurant.print_flavors()
        case 2:
            # second
            ice_cream_restaurant = IceCreamStand('Cool Ice Creams', 'западная', 4.5,
                                                 ['пломбир', 'сливочное', 'молочное', 'крем-брюле', 'шербет', 'мягкое'],
                                                 'На Вознесенском', '10:00 - 20:00')
            ice_cream_restaurant.describe_restaurant()
            ice_cream_restaurant.print_location_and_time()
            ice_cream_restaurant.print_flavors()
            print()
            ice_cream_restaurant.add_flavors()
            ice_cream_restaurant.print_flavors()
            print()
            ice_cream_restaurant.del_flavors()
            ice_cream_restaurant.print_flavors()
            print()
            ice_cream_restaurant.search_flavor()
            print()
            ice_cream_restaurant.stick_ice_cream('Ванильное')
            ice_cream_restaurant.soft_ice_cream('Шоколадное', 'Мята')

        case 3:
            def create_rest():
                ice_cream_restaurant = IceCreamStand(e1.get(), e2.get(), e3.get(),
                                                     ['пломбир', 'сливочное', 'молочное', 'крем-брюле', 'шербет',
                                                      'мягкое'],
                                                     e4.get(), e5.get())
                label2 = Label(window, text=ice_cream_restaurant.restaurant_name, font='times 18 bold')
                label2.place(x=450, y=140)
                label3 = Label(window, text=f'Кухня: {ice_cream_restaurant.cuisine_type}', font='times 13')
                label3.place(x=470, y=220)
                label4 = Label(window, text=f'Рейтинг: {ice_cream_restaurant.rating_points}', font='times 13')
                label4.place(x=470, y=250)
                label11 = Label(window, text=f'Локация: {ice_cream_restaurant.location}', font='times 13')
                label11.place(x=470, y=280)
                label12 = Label(window, text=f'Время работы: {ice_cream_restaurant.time}', font='times 13')
                label12.place(x=470, y=310)
                label13 = Label(window, text='Список блюд:', font='times 13')
                label13.place(x=470, y=350)
                flavors_text = ''
                for i in range(0, len(ice_cream_restaurant.flavors), 2):
                    if i + 1 < len(ice_cream_restaurant.flavors):
                        flavors_text += f'{ice_cream_restaurant.flavors[i]}, {ice_cream_restaurant.flavors[i + 1]}\n'
                    else:
                        flavors_text += f'{ice_cream_restaurant.flavors[i]}\n'
                label14 = Label(window, text=flavors_text, font='times 13', justify='left')
                label14.place(x=470, y=390)

            window = Tk()
            window.geometry('900x700')
            label1 = Label(window, text='Создаем ресторан', font='times 25 bold')
            label1.place(x=450, y=50, anchor='center')

            label5 = Label(window, text='Выберите действие:', font='times 17')
            label5.place(x=20, y=140)

            label6 = Label(window, text='Название ресторана:', font='times 12')
            label6.place(x=20, y=200)
            e1 = Entry(window)
            e1.place(x=20, y=230)

            label7 = Label(window, text='Кухня:', font='times 12')
            label7.place(x=20, y=270)
            e2 = Entry(window)
            e2.place(x=20, y=300)

            label8 = Label(window, text='Рейтинг:', font='times 12')
            label8.place(x=20, y=340)
            e3 = Entry(window)
            e3.place(x=20, y=370)

            label9 = Label(window, text='Локация:', font='times 12')
            label9.place(x=20, y=410)
            e4 = Entry(window)
            e4.place(x=20, y=440)

            label10 = Label(window, text='Время работы:', font='times 12')
            label10.place(x=20, y=480)
            e5 = Entry(window)
            e5.place(x=20, y=510)

            b = Button(window, text='Создать', width=20, command=create_rest)
            b.place(x=20, y=580)

            window.mainloop()
        case _:
            print('такого задания нет!')
    pass
