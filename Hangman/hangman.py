import random
import string


def main():
    word_list = ["python", "java", "kotlin", "javascript", "cplusplus"]
    random.seed()
    ans = random.choice(word_list)
    hint = ''.center(len(ans), '-')
    tries = 0
    repeats = ''

    while tries != 8:
        print()
        print(hint)

        if hint == ans:
            print('You guessed the word')
            break
        letter = input("Input a letter: >").strip()

        if len(letter) > 1:
            print('You should input a single letter')
            continue

        if letter not in string.ascii_lowercase:
            print('It is not an ASCII lowercase letter')
            continue

        if letter in repeats:
            print('You already typed this letter')
            continue

        if letter in ans:
            if letter not in hint:
                for i, j in enumerate(ans):
                    if j == letter:
                        h_lst = list(hint)
                        h_lst[i] = letter
                        hint = ''.join(h_lst)
            else:
                print('You already typed this letter')
        else:
            print('No such letter in the word')
            tries += 1
            repeats += letter

    if hint == ans:
        print('You survived!\n')
    else:
        print('You exhausted all your 8 tries')
        print('You are hanged!\n')


print("Welcome to H A N G M A N")
print("Rules of the game: You need to guess the word to survive or else you will be hanged")
print("Hint: A language which machines understand")
game = "play"
while game != "exit":
    game = input('Type "play" to play the game, "exit" to quit: ')
    if game == "play":
        main()
    elif game != "exit":
        print("Wrong entry! please type again")
