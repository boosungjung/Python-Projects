import datetime

today = datetime.date.today()
x = today.strftime(' (%d, %b %Y)')
goal = 30
total = 0
with open('hours.txt', 'a') as f:
    input_hours = int(input("How many hours did you do?"))
    string_input = str(input_hours)

    fw = f.write(string_input + x +"\n")

with open('hours.txt') as c:
    for i in c:
        total = total + int(i[0:2])
    print("Total hours completed this month: ", total)
    print("Hours left this month: ", goal-total)







