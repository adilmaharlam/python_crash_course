favorite_places = {
    'Rafael': ['Baku', 'Istanbul', 'Moscow'],
    'Amin': ['Celilabad', 'Ganja', 'Sumgait'],
    'Hesen': ['Anashkin', 'Lankaran', 'Shaki']
}

for name, place in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for p in place:
        print(f"- {p}")
        