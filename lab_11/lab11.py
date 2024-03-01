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


if __name__ == "__main__":
    ex = int(input('Введите номер задания: '))
    match ex:
        case 1:
            # first
            newRestaurant = Restaurant('La Trattoria', 'итальянская', None)
            print("Название ресторана:", newRestaurant.restaurant_name)
            print("Тип кухни: ", newRestaurant.cuisine_type)
            newRestaurant.describe_restaurant()
            newRestaurant.open_restaurant()
        case 2:
            # second
            newRestaurant_1 = Restaurant('The Golden Spoon', 'итальянская', None)
            newRestaurant_1.describe_restaurant()
            newRestaurant_2 = Restaurant('The Rustic Kitchen', 'русская', None)
            newRestaurant_2.describe_restaurant()
            newRestaurant_3 = Restaurant('The Golden Spoon', 'французская', None)
            newRestaurant_3.describe_restaurant()
        case 3:
            # third
            newRestaurant = Restaurant('La Trattoria', 'итальянская', 3.4)
            newRestaurant.describe_restaurant()
            point = float(input('Введите обновленный рейтинг: '))
            newRestaurant.rating(point)
            newRestaurant.describe_restaurant()
        case _:
            print('такого задания нет!')
