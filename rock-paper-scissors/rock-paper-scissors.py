import random

print('Welcome to Rock-Paper-Scissors Game')
print('You can play with default options <rock,paper,scissors> or')
print('you can create your own options <rock,paper,scissors,lizard,spock> or any other')
rating = 0
name = input('Please enter your name: ')
print('Hello,', name)
game_options = input('press enter for default game options or create your own: ').strip().split(',')
if game_options == ['']:
    game_options = ['rock', 'paper', 'scissors']  # 'lizard', 'spock']
print("Okay, let's start the game with the below game options")
print(*game_options, sep='<-->')

with open('rating.txt', 'r') as scores:
    for line in scores.readlines():
        if name in line:
            rating = int(line.split()[1])

while True:
    user_in = input("You choose: >").strip()
    if user_in == "!exit":
        print('Bye!')
        break
    elif user_in == "!rating":
        print('Your rating:', rating)
        continue
    elif user_in not in game_options:
        print('Invalid input')
        continue

    random.seed()
    comp_out = random.choice(game_options)

    if user_in == comp_out:
        print(f"There is a draw ({comp_out})")
        rating += 50
    else:
        idx = game_options.index(comp_out)
        rule_list = []
        if idx == len(game_options) - 1:
            rule_list.extend(game_options[:idx])
        elif idx == 0:
            rule_list.extend(game_options[idx + 1:])
        else:
            rule_list.extend(game_options[idx + 1:])
            rule_list.extend(game_options[:idx])

        uidx = rule_list.index(user_in)
        if uidx < len(rule_list) / 2:
            print(f'Well done. The computer chose {comp_out} and failed')
            rating += 100
        else:
            print(f"Sorry, but the computer chose {comp_out}")




