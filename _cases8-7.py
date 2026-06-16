def make_album(name, title, number=None):
    album = {'Name': name, 'Title': title}
    if number:
        album['number'] = number
    return album

print(make_album('rihanna', 'diamonds'))
print(make_album('travis scoot', 'fein'))
print(make_album('eminem', 'superman', 14))