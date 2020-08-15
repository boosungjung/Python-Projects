a_file = open("random words text")

list_of_lists = []
randword = a_file.read()
lines = randword.split("\n")
for line in lines:
  list_of_lists.append(line)

a_file.close()

print(list_of_lists)