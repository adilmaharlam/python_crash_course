aliens = []

for alien_number in range(30):
    new_aliens = {'color': 'green', 'points': 10, 'speed': 'slow'}
    aliens.append(new_aliens)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 15
        alien['speed'] = 'medium'
    

print("...")
print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:5]:
    print(alien)

def change_alien_color(alien, new_color):
    alien['color'] = new_color
    if new_color == 'red':
        alien['points'] = 20
        alien['speed'] = 'fast'
    elif new_color == 'yellow':
        alien['points'] = 15
        alien['speed'] = 'medium'
    else:
        alien['points'] = 10
        alien['speed'] = 'slow'