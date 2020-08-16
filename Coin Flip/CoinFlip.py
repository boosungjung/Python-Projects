import random

bot_choice = 0
bank = 15.00
bet = 0.00
player = ''
wrong_input = ["I said h or t. You skunked?", "h or t. Enter again!", "can you type properly?"]
poor_input = ["You're poor. Enter again!", "Lmao you're poor", "You think you can trick me? Enter again!"]
print("Welcome to the Coin Flip game!")
print("You will start with", bank, "coins")
print("Your betted coins will double if you win. If you lose, you will lose your betted coins.")
print("Try and get as much coins as you can. If your bank reaches 0 you lose the game.")
print("---------------------------------------------------------------------------------------------------------------")
print("~Milestones~\n"
      "~Bronze: 100~\n"
      "~Silver: 200~\n"
      "~Gold: 300~\n"
      "~Diamond: 500~")
print("---------------------------------------------------------------------------------------------------------------")

while bank > 0.00:

    print("You have", bank, "coins!")
    bet = float(input("How much would you like to bet?"))
    player = str(input("Enter h for Heads or t for Tails"))
    if bet <= bank:
        bot_choice = random.randint(1, 2)
        if player == 'h':
            if bot_choice == 1:
                print("You Win!\n")
                bank += bet
            else:
                print("You Lose!\n")
                bank -= bet

        elif player == 't':
            if bot_choice == 2:
                print("You Win!\n")
                bank += bet
            else:
                print("You Lose!\n")
                bank -= bet
        else:
            print(random.choice(wrong_input), "\n")
    else:
        print(random.choice(poor_input), "\n")
print("\nOops you went bankrupt!\nMaybe that's why you shouldn't gamble")
exit = input("Press enter to exit")
