from datetime import date

names = ['Hiro', 'Joel', 'Leslie', 'Natsuki', 'Josiah', 'Mary', 'Margaret', 'Andrew', 'Peng Peng', 'Jessica', 'Edward Lee', 'Noelle Lee', 'Shamala', 'Reshma', 'BooSung', 'Jennifer', 'Suna', 'Koichi', 'Yuriya']
current_date = date.today()
present = []
position = 0
print("Enter 1 for Present and any other number for Absent")
try:
    for i in names:
        print(i)
        attendance = int(input(":"))
        if attendance == 1:
            present.append(i)
    print("Setapak Group Attendance on", current_date)
    for x in present:
        position += 1
        print(str(position)+'.', x)
    cont = input("Press enter to close")
except ValueError:
    print("Only integers allowed")
    cont = input("Press enter to close")
