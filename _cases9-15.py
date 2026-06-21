from random import choice

lottery_pool = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')
my_ticket = (3, 7, 'B', 'D')

num_tries = 0
won = False

while not won:
    current_poll = []
    for _ in range(4):
        current_poll.append(choice(lottery_pool))
        num_tries += 1

    won = True
    for number in my_ticket:
        if number not in current_poll:
            won = False
            break

print(f"It took {num_tries} tries to win the lottery with ticket {my_ticket}.")