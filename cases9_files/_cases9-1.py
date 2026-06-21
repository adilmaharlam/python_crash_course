class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name}")
        print(f"Cuisine type is {self.type}")

    def open_restaurant(self):
        print(f"Restaurant is open")

x1 = Restaurant('Bomba mekan', 'doner')
x2 = Restaurant('Quzzetti', 'traditional cuisine')
x3 = Restaurant('Kompas', 'sushi')

x1.describe_restaurant()
x2.describe_restaurant()
x3.describe_restaurant()
