cities = {
    'baku': {
        'country': 'azerbaijan',
        'continent': 'asia',
        'population': 2_300_000,
        'language': 'azerbaijani',
        'fact': 'baku is the lowest-lying national capital in the world, sitting 28 m below sea level.',
        'landmarks': ['flame towers', 'maiden tower', 'heydar aliyev center'],
    },
    'tokyo': {
        'country': 'japan',
        'continent': 'asia',
        'population': 13_960_000,
        'language': 'japanese',
        'fact': 'tokyo was originally a fishing village called edo before becoming the capital in 1868.',
        'landmarks': ['tokyo tower', 'shibuya crossing', 'senso-ji temple'],
    },
    'istanbul': {
        'country': 'turkey',
        'continent': 'europe & asia',
        'population': 15_460_000,
        'language': 'turkish',
        'fact': 'istanbul is the only city in the world that spans two continents.',
        'landmarks': ['hagia sophia', 'blue mosque', 'grand bazaar'],
    },
}

line = '=' * 60

for city_name, info in cities.items():
    print(f"\n{line}")
    print(f"  {city_name.upper()}")
    print(line)
    print(f"  {'Country:':<12} {info['country'].title()}")
    print(f"  {'Continent:':<12} {info['continent'].title()}")
    print(f"  {'Population:':<12} {info['population']:,}")
    print(f"  {'Language:':<12} {info['language'].title()}")
    print(f"  {'Fact:':<12} {info['fact'].capitalize()}")
    print(f"  {'Landmarks:':<12}", end='')
    for i, landmark in enumerate(info['landmarks']):
        if i == 0:
            print(f" {landmark.title()}")
        else:
            print(f"  {'':<12} {landmark.title()}")