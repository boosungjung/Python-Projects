with open("hours.txt") as f:
    cal = 0
    total = 0
    for i in f:
        total = total + int(i[0:2])
        print(total)