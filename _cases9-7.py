class User:
    def __init__(self, first_name, last_name, age, location):
        self.fn = first_name
        self.ln = last_name
        self.age = age
        self.loc = location

    def describe_user(self):
        print(f"The full name of this user is {self.fn} {self.ln}‚ age ={self.age}, location ={self.loc}")
    def greet_user(self):
        print(f"Hello {self.fn} {self.ln}")

class Admin(User):

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"\nYour privileges is:")
        for pr in self.privileges:
            print(f"- {pr}")

admin = Admin('Adil', 'Məhərləmov', 20, 'baku')
admin.describe_user()
admin.show_privileges()
