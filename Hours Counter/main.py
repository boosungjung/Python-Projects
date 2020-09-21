import datetime
import time
import os

today = datetime.date.today()
x = today.strftime(' (%d, %b %Y)')
goal = 30


class main():

    def __init__(self):
        global goal
        size = os.path.getsize('hours.txt')
        if size == 0:
            goal = int(input("What is your hour goal for this month?"))

    def reset(self):
        print("deleting all data...")
        with open('hours.txt', 'r+') as d:
            d.truncate(0)
        time.sleep(1)
        print("completed")

    def input_hours(self):
        with open('hours.txt', 'a') as f:
            input_hours = int(input("How many hours did you do?\n"))
            string_input = str(input_hours)
            if input_hours < 1:
                print('')
            else:
                fw = f.write(string_input + x +"\n")

    def calc(self):
        total = 0
        with open('hours.txt') as c:
            for i in c:
                total = total + int(i[0:2])
            print("Total hours completed this month: ", total)
            print("Hours left this month: ", goal-total)


user = input("1.Record hours 2.Calculate remaining hours 0.Reset data\n")
u = main()

if user == "1":
    u.input_hours()
    u.calc()
elif user == "0":
    confirm = input("type confirm if you want to delete all data?\n")
    if confirm == "confirm":
        u.reset()
elif user == "2":
    u.calc()




















