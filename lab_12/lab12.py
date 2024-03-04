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
            pass
            # в реализации
            # window = Tk()
            # window.geometry('900x700')
            # label1 = Label(window, text='Название заведения', font='times 25 bold')
            # label1.place(x=450, y=50, anchor='center')
            # label2 = Label(window, text='MENU', font='times 20 bold')
            # label2.place(x=600, y=140)
            # label3 = Label(window, text='ванильное', font='times 12')
            # label3.place(x=600, y=200)
            # label4 = Label(window, text='шоколадное', font='times 12')
            # label4.place(x=600, y=230)
            #
            # label5 = Label(window, text='Выберите действие', font='times 17')
            # label5.place(x=20, y=140)
            #
            # label6 = Label(window, text='Добавить мороженное', font='times 12')
            # label6.place(x=20, y=200)
            # e1 = Entry(window)
            # e1.place(x=20, y=230)
            #
            # label7 = Label(window, text='Удалить', font='times 12')
            # label7.place(x=20, y=270)
            # e2 = Entry(window)
            # e2.place(x=20, y=300)
            #
            # window.mainloop()
        case _:
            print('такого задания нет!')
    pass
