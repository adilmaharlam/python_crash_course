current_users = ['adil','amin','burxan','hesen','rafael']
new_users = ['eli', 'ugur','ekber','hesen','rafael']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users:
        print(f"'{user}' is already taken. Please enter a new username.")
    else:
        print(f"'{user}' is available!")