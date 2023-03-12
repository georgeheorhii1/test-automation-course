def read_side():
    return float(input("Enter the length of a side (must be a number): "))


def is_square(side1, side2, side3, side4):
    return side1 == side2 == side3 == side4


def is_rectangle(side1, side2, side3, side4):
    diagonal1 = (side1 ** 2 + side2 ** 2) ** 0.5
    diagonal2 = (side3 ** 2 + side4 ** 2) ** 0.5
    return diagonal1 == diagonal2


def rectangle_area(side1, side2):
    return side1 * side2


def square_area(side):
    return side ** 2


side1 = read_side()
side2 = read_side()
side3 = read_side()
side4 = read_side()

if is_square(side1, side2, side3, side4):
    print("The quadrilateral is a square.")
else:
    if not is_rectangle(side1, side2, side3, side4):
        print("The quadrilateral is neither a square nor a rectangle.")
    else:
        area = rectangle_area(side1, side2)
        print(f"The quadrilateral is a rectangle. Its area is {area:.2f}.")

# Task2

import random


def create_email(domains, names):
    last_name = random.choice(names)
    random_number = random.randint(100, 999)
    random_domain = random.choice(domains)
    email = f"{last_name}.{random_number}@.{random_domain}"
    return email


names = ["king", "miller", "kean"]
domains = ["net", "com", "ru"]
e_mail = create_email(domains, names)
print(e_mail)
