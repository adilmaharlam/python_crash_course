def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

while True:
    print("\nEnter 'q' at any time to quit.")
    artist = input("Artist name: ")
    if artist == 'q':
        break
    title = input("Title: ")
    if title == 'q':
        break

    album = make_album(artist, title)