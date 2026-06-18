def show_messages(messages, sent_messages):
    while messages:
        current_mesage = messages.pop
        print(current_mesage)
        sent_messages.append(current_mesage)

text_messages = [
    "hey, are we still on for lunch?",
    "i finished the report, sending it over now",
    "running 10 minutes late, sorry!",
]

sent_messages = []

show_messages(text_messages, sent_messages)
print("\nUnsent messages:")
print(text_messages)

print("\nSent messages:")
print(sent_messages)