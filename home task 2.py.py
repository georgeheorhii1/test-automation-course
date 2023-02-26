import random
from typing import Tuple

# Task 1
min = random.randrange(0, 100)

print("Random number is " + str(min))
print("Quoter is " + str((1 + min // 15)))

# Task 2
birth_month: str = input('Enter the number of the birth month:')
winter = (12, 1, 2)
spring = (3, 4, 5)
summer = (6, 7, 8)
autumn = (9, 10, 11)

if birth_month in str(winter):
    print('Winter - It was snowing outside the window.')
if birth_month in str(spring):
    print('Spring - Everything around blossomed')
if birth_month in str(summer):
    print('Summer - Children enjoyed the summer vacation')
if birth_month in str(autumn):
    print('Autumn - Everything around lit up with bright colors')
else:
    print('Month is not defined')

# Task 3

num = random.randint(1, 100)

if num % 6 == 0:
    print(f"Number {num} is divisible by 6")
else:
    print(f"Number {num} is not divisible by 6")

# Task 4

x = float(input("Please provide the following coordinate for: x="))
y = float(input("Please provide the following coordinate for: y="))
if x>0 and y>0:
    print('I. First quadrant')
elif x<0 and y>0:
    print('II. Second quadrant')
elif x<0 and y<0:
    print('III. Third quadrant')
elif x>0 and y<0:
    print('IV. Fourth quadrant')
elif x == 0 and y == 0:
    print("The origin.")
elif x == 0:
    print("The y-axis.")
elif y == 0:
    print("The x-axis.")














