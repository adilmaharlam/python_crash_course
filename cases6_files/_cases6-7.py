person = {
    'person1': {
    'name': 'Rafael',
    'surname': 'Zeynalov',
    'age': '20',
    'city': 'Baku'
},
    'person2': {
    'name': 'Amin',
    'surname': 'Nagizade',
    'age': '19',
    'city': 'Celilabad'
},
    'person3': {
    'name': 'Hesen',
    'surname': 'Talibov',
    'age': '18',
    'city': 'Anashkin'
    }
}

people = [person['person1'], person['person2'], person['person3']]
for person in people:
    print(f"\nName: {person['name']}")
    print(f"Surname: {person['surname']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")