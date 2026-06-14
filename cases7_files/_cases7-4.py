prompt = "\nWhat do you want your pizza? "
prompt += "\nIf it is okey write 'quit' "

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"You add {message.title()}")






