add = '54200 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur, Malaysia'
undivided = []
street = []
unit = []
space = []


class main:

    def __init__(self):
        global undivided,x
        undivided = input(":")
        x = 0  #position of space
        for i in undivided:
            x += 1
            street.append(i)
            if i == '	':  #	special space
                print("space", x) #if special space initiate function to seperate street and unit


    def divide(self):
        print("Hi")
        for j in undivided[29:]:
            unit.append(j)
            print("unit",unit)



while True:
    s = main()
    s.divide()
