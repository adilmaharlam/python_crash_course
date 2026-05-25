pet_dic = {
    'pet1': {
        'name': 'Rex',
        'type': 'dog',
        'owner': 'Alice'
    },
    'pet2': {
        'name': 'Whiskers',
        'type': 'cat',
        'owner': 'Bob'
    },
    'pet3': {
        'name': "Goldie",
        'type': 'fish',
        'owner': 'Charlie'
    }
}

pets = [pet_dic['pet1'], pet_dic['pet2'], pet_dic['pet3']]
for pet in pets:
    print(f"\nName: {pet['name']}")
    print(f"Type: {pet['type']}")
    print(f"Owner: {pet['owner']}")
    