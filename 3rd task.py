user_input = int(input("Enter the Number for cheak : "))

for i in range(2,user_input):

    if user_input % i == 0:
        print("Given Number is not a prime number")
        break
else:
     print("Given Number is a prime number")




