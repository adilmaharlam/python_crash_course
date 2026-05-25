cities = {
    'Baku': {
        'country': 'Azerbaijan',
        'population': '2.3 million',
        'fact': 'Baku is the largest city on the Caspian Sea and offers a mix of modern and historical architecture.'
    },
    'Edmonton': {
        'country': 'Canada',
        'population': '1 million',
        'fact': 'Edmonton is known for its vibrant arts scene and is home to the largest mall in North America, West Edmonton Mall.'
    },
    'Massachusetts': {
        'country': 'USA',
        'population': '6.9 million',
        'fact': 'Massachusetts is home to the prestigious Harvard University and is known for its rich history and cultural heritage.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"-Country: {info['country']}")
    print(f"-Population: {info['population']}")
    print(f"-Fact: {info['fact']}")