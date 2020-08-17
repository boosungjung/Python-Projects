guess = 0

def hangman():
    global game
    if guess == 1:
        print('_______')
        print('|  |')
        print('|')
        print('|')
        print('|')
        print('|______')

    elif guess == 2:
        print('_______')
        print('|  |')
        print('|  0')
        print('|')
        print('|')
        print('|______')

    elif guess == 3:
        print('_______')
        print('|  |')
        print('|  0')
        print('|  |')
        print('| / \ ')
        print('|______')

    elif guess == 4:
        print('_______')
        print('|  |')
        print('| _0')
        print('|  |')
        print('| / \ ')
        print('|______')

    elif guess == 5:
        print('_______')
        print('|  |')
        print('| _0_')
        print('|  |')
        print('| / \ ')
        print('|______')
        print("Game Over")
        game = False


word_choice = input("Choose a word: ")
chosen_word_list = []
word_dash = []

#purpose of this is to store the chosen word into a list and output dashes corresponding to the length of the word
for i in word_choice:
    chosen_word_list.append(i) #stores word in a list
    word_dash.append('_') #stores dashes corresponding to the length of the word

print(word_dash)
i = 0 #counter to check for duplicate letters
length = len(chosen_word_list)
game = True
while game:
    player_guess = input("Guess a letter")
    if len(player_guess) == 1:
        if player_guess in chosen_word_list: #checks if guessed word is in the chosen_word_list
            while i < length:
                if player_guess == chosen_word_list[i]:
                    word_dash[i] = player_guess
                i += 1
            i = 0
            print(word_dash)

            if chosen_word_list == word_dash:
                print("You Win!")
                game = False
        else:
            guess += 1
            hangman()
    else:
        print("enter a single letter")

