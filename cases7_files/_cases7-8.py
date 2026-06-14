sandwich_orders = ['chicken sandwich', 'beef sandwich', 'veggie sandwich']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nI made the following sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)