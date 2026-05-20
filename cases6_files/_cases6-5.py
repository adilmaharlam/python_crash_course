rivers = {
    'egypt': 'nile',
    'azerbaijan': 'araz',
    'brazil': 'amazon'
}

for key, value in rivers.items():
    print(f"The {value.title()} runs through {key.title()}")

print()

for key in rivers.keys():
    print(f"{key.title()}")

print()

for value in rivers.values():
    print(f"{value.title()}")

