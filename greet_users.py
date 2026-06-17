def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
    
usernames = ['adil', 'amin','burxan', 'hesen']
greet_users(usernames)