favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

should_take_poll = ['jen', 'edward', 'adil', 'leyla', 'sarah', 'tural']

for name in should_take_poll:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll!")
    else:
        print(f"{name.title()}, please take our favorite languages poll!")