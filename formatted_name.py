def get_formatted_name(first_name, last_name, middle_name =''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
    
muisican = get_formatted_name('jimi', 'hendrix')
print(muisican)
muisican = get_formatted_name('john', 'hooker', 'lee')
print(muisican)