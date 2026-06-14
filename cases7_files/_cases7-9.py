sandwich_orders = ['pastrami', 'chicken', 'pastrami', 'beef', 'pastrami', 'veggie']
print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)