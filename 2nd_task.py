inputs = int(input("enter the number or press enter to quit: "))

list = []

while True:
    if inputs == "":
        print("enter again")
        break
    else:
         list.append(inputs)
         inputs = int(input("enter the number or press enter to quit: "))
print(list)
