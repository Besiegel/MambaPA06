"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

def generate_random_word():
    import random
    filename = "hangman_words.txt"
    file = open(filename,"r")
    text = file.read()
    words = text.split()
    alpha = random.choice(words).casefold()
    return alpha
word = generate_random_word()

def play_hangman():
    want_to_play = True


    while (want_to_play):
        guessed_letters = []
        guesses_left = 6
        letter_length = 0
        unknown_word = []
        word = generate_random_word()
        letter_list = list(word)
        
#Defines unknown word as a list of -'s equal to the length of the word       
        while letter_length < len(letter_list):
            unknown_word.append("-")
            letter_length += 1
            
        print(unknown_word)
        letter = input("Guess a single letter").casefold()
        done = False
        while done == False:
            if letter in guessed_letters:
                print("You have already guessed this letter")
                guesses_left += -1
                print("You have",guesses_left,"guesses left")
            elif letter not in word:
                guessed_letters.append(letter)
                print("That letter is not in the word")
                guesses_left += -1
                print("You have",guesses_left,"guesses left")
            elif letter != "":
                guessed_letters.append(letter)
                print("That letter is in the word")
            gamma = all(elem in guessed_letters  for elem in letter_list)
            if gamma == True:
                done = True
                print("You win!")
            elif guesses_left == 0:
                done = True
                print("You lose!")
            elif letter == "":
                print("Space is not a letter")
                guesses_left += -1
                print("You have",guesses_left,"guesses left")
            if letter in word and letter != "":
                beta = letter_list.index(letter)
                correct_letter = letter
                unknown_word[beta] = correct_letter
                print(unknown_word)
                if gamma == False:
                    letter = input("Guess another letter").casefold()
            elif gamma != True:
                letter = input("Guess another letter").casefold()
        want_to_play = input("Do you want to play again? Y or N?")
        if want_to_play == "Y":
            want_to_play = True
        elif want_to_play == "N":
            want_to_play = False
        else:
            want_to_play = False

if __name__ == '__main__':
    play_hangman()
