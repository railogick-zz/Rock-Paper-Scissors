# Write your code here
import random
import math


def get_current_ratings():
    users = {}
    with open('rating.txt', 'r', encoding='utf-8') as rating:
        for line in rating:
            name, rate = line.rstrip().split()
            users[name] = int(rate)
    return users


def record_ratings(users):
    with open('rating.txt', 'w', encoding='utf-8') as rating:
        for k, v in users.items():
            rating.write(str(k) + ' ' + str(v) + '\n')


# Game Start
scores = get_current_ratings()
user = input('Enter your name: ')
if user not in scores:
    scores[user] = 0
print(f'Hello, {user}')

game_input = input()
if game_input:
    game = [x.strip() for x in game_input.split(',')]
else:
    game = ['rock', 'paper', 'scissors']
print('Okay, let\'s start')

while True:
    player_choice = input()
    comp = random.choice(game)
    if player_choice == '!rating':
        print(scores[user])
        continue
    elif player_choice == '!exit':
        print('Bye!')
        break

    n = len(game)
    p1 = game.index(player_choice)
    p2 = game.index(comp)

    winner = (p1 - p2) % n

    if winner == 0:
        print(f'There is a draw ({player_choice})')
        scores[user] += 50
    elif winner < math.ceil(n/2):
        print(f'Well done. Computer chose {comp} and failed')
        scores[user] += 100
    else:
        print(f'Sorry, but computer chose {comp}')

record_ratings(scores)




