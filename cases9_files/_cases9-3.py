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

user1 = User('adil', 'meherlemov', 20, 'baku')
user2 = User('nigar', 'kocerli', 29, 'baku')
user3 = User('elon', 'musk', 53, 'austin')

for user in (user1, user2, user3):
    user.describe_user()
    user.greet_user()