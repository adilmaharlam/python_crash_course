def make_sandwiches(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwiches('tomato', 'meat', 'egg', 'haviar')
make_sandwiches('cheese', 'mustard')
make_sandwiches('ham', 'swiss', 'pickles', 'mayo')
