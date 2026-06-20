class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name}")
        print(f"Cuisine type is {self.type}")

    def open_restaurant(self):
        print(f"Restaurant is open")
        
class  IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'pistachio']

    def display_flavors(self):
        print("\nWe have the following flavors available:")
        
        for flavor in self.flavors:
            print(f"- {flavor}")

stand = IceCreamStand('Frosty Scoops','ice cream')
stand.describe_restaurant()
stand.display_flavors()