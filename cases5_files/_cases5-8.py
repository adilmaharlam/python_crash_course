names = ['admin','burxan','amin','hesen','rafael']
for name in names:
    if name == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"\nHello {name.title()},thank you for logging in again")