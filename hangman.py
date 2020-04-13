import random

## .ascii_uppercase is the command for alphabet ###

ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


words = ['hello', 'snow', 'yesterday', 'afraid', 'orange', 'magnificent']

def randomword(words):
    words = random.choice(words)
    while '' in words:
        word = random.choice(words)
        return word.upper()
def hangman_game():
    word = randomword(words)
    word_letters = word.split()
    AtoZ = ascii_uppercase.split() ##list of all letters in alphabet
    used_letters = []

    while len(word_letters) > 0:
        # turns each iterated letter into a string

        print('you have used:', .join(used_letters), 'and have', turns, 'number of lives')
        word_list = [letter if letter in used_letters else '?' for letter in word]
        print('current word:', .join(word_list))
        user_letter = input('guess a letter').upper()
        if word_letters in AtoZ:
            if word_letters not in used_letters:
                used_letters.append(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                turns -= 1
                print('Letter is not in word')


        elif user_letter in used_letters:
            print("Please enter another letter. You have already used that.")

        else:
            print("invalid character")

    if turns ==0:
        print('You died. The word was', word)
    else:
        print('you guessed', word, 'congrats!')

print(hangman_game())
