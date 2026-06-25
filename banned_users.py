banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


if user in banned_users:
    print(f"{user.title()}, you are banned from posting a response.")
