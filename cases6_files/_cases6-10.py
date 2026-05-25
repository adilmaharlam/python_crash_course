fnumbers = {
    'adil': [11, 12, 13],
    'burxan': [22, 23, 24],
    'hesen': [33, 34, 35],
    'amin': [44, 45, 46],
    'rafael': [55, 56, 57]
}

for name, values in fnumbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for value in values:
        print(f"- {value}")