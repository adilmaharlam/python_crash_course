with open('guest_book.txt', 'w') as f:
    while True:
        name = input("Enter your name (or 'q' to quit): ")
        if name == 'q':
            break
        f.write(name + '\n')
        f.flush()  # hər addan sonra dərhal fayla yaz
        print(f"Added {name} to guest book.")

print("\nGuest book saved! Here are the entries:")
with open('guest_book.txt') as f:
    print(f.read())