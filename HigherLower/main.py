from game_data import data
from art import logo, vs
from random import choice
from replit import clear


def choising():
    escolha = choice(data)
    data.remove(escolha)
    return escolha


def winner(a, b):
    if a['follower_count'] > b['follower_count']:
        return a
    else:
        return b


print(len(data))


def game():
    pessoa1 = choising()
    score = 0
    print(logo)
    while True:
        pessoa2 = choising()
        print(f"Compare A: {pessoa1['name']}, a {pessoa1['description']}, from {pessoa1['country']}. ")
        print(vs)
        print(f"Against B: {pessoa2['name']}, a {pessoa2['description']}, from {pessoa2['country']}. ")
        most_followed = winner(pessoa1, pessoa2)
        while True:
            guess = input('Who has more followers? Type A or B: ').lower()
            if guess == 'a' or guess == 'b':
                break
            else:
                print('Type a valid guess!!!')
        if guess == 'a':
            guess = pessoa1['name']
        else:
            guess = pessoa2['name']
        clear()
        if guess != most_followed['name']:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break
        else:
            pessoa1 = pessoa2
            score += 1
            print(logo)
            print(f'You are right! Current score: {score}.')
            print(len(data))


game()
