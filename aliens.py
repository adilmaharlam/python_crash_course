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