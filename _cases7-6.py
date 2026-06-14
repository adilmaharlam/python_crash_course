prompt = "\nWhat topping would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished.) "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)



prompt = "\nWhat topping would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished.) "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)



prompt = "\nWhat topping would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)