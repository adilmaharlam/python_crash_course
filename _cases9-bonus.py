from random import choice

lottery_pool = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')
my_ticket = (3, 7, 'B', 'D')

num_simulations = 1_000_000
wins_on_first_try = 0

for _ in range(num_simulations):
    current_pull = []
    for _ in range(4):
        current_pull.append(choice(lottery_pool))

    won = True
    for number in my_ticket:
        if number not in current_pull:
            won = False
            break

    if won:
        wins_on_first_try += 1

probability = wins_on_first_try / num_simulations
print(f"Won on first try: {wins_on_first_try} out of {num_simulations} simulations.")
print(f"Estimated probability of winning in one try: {probability:.6%}")