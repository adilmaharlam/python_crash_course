class User:
    def __init__(self, first_name, last_name, age, location):
        self.fn = first_name
        self.ln = last_name
        self.age = age
        self.loc = location
        self.login_a = 0

    def describe_user(self):
        print(f"The full name of this user is {self.fn} {self.ln}‚ age ={self.age}, location ={self.loc}")


    def greet_user(self):
        print(f"Hello {self.fn} {self.ln}")


    def increment_login_attempts(self):
        self.login_a += 1


    def reset_login_attempts(self):
        self.login_a = 0


user1 = User('adil', 'meherlemov', 20, 'baku')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_a}")

user1.reset_login_attempts()
print(f"Login attempts: {user1.login_a}")