import random
dice_quantity = int(input("Enter the Number: "))

total = 0

for i in range(dice_quantity):
    roll = random.randint(1, 6)
    total += roll

print(f"total sum of dice rolls are {total}.")