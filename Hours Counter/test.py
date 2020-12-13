with open('hours.txt','r') as read:
    for i, line in enumerate(read):
        if i > 0:
            print(line[0:2])
