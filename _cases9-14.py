from random import choice

lottery_pool = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')

wining_numbers = []
for _ in range(4):
    wining_numbers.append(choice(lottery_pool))

print("The four winning numbers/letters are:")
for number in wining_numbers:
    print(number)

print("\nIf your ticket matches these 4 numbers/letters, you win!")