import random
dice_quantity = int(input("Enter the Number of dices want to roll: "))

total = 0

for i in range(dice_quantity):
    roll = random.randint(1, 6)
    total += roll

print(f"total sum of dice rolls are {total}.")