import random
print("Welcome to the Rock scissors paper game")
w = 0
l = 0
d = 0
replay = 1
player = int(input("Choose your option 1. Rock 2. Scissors 3. Paper"))
while replay <= 300000:
    com = random.randint(1, 3)
    if player == 1:
        if com == 1:
            print("Draw")
            d += 1
        elif com == 2:
            print("You Win!")
            w += 1
        else:
            print("You Lose!")
            l += 1

    if player == 2:
        if com == 1:
            print("You Lose!")
            l += 1
        elif com == 2:
            print("Draw!")
            d += 1
        else:
            print("You Win!")
            w += 1

    if player == 3:
        if com == 1:
            print("You Win!")
            w += 1
        elif com == 2:
            print("You Lose!")
            l += 1
        else:
            print("Draw!")
            d += 1
    replay = replay + 1
print("win", w, "lose", l, "draw", d, "win percentage", w/(d+l+w))
