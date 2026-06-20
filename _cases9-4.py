class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_surved = 0

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name}")
        print(f"Cuisine type is {self.type}")

    def open_restaurant(self):
        print(f"Restaurant is open")

    def set_number_served(self, number_served):
        self.number_surved = number_served

    def increment_number_served(self, plus_number):
        self.number_surved += plus_number


restaurant = Restaurant('Bomba mekan', 'doner')

print(f"Number served: {restaurant.number_surved}")

restaurant.set_number_served(225)
print(f"Number served: {restaurant.number_surved}")

restaurant.increment_number_served(37)
print(f"Number served: {restaurant.number_surved}")