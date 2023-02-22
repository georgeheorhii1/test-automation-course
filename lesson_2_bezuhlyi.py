from math import pi


# Task #1
name = input('Please enter Your name:')
surname = input('Please enter Your surname:')
print(name + ' ' + surname)
ns = surname + ' ' + name
print(ns.lower())
print(ns.upper())
print(ns.title())

count = 0;
while count < 4:
 print(ns)
 count += 1

new_name = name + '\t' + surname
new_name_2 = name + '\n' + surname
print(new_name)
print(new_name_2)
print(name.rstrip())
print(name.lstrip())

# Task #2
# програму для обчислення довжини кола та площі круга за введеним радіусом.
# центр круга = о.
# точка на коемке окружности = А
# Radius = from O to A(OA)
# Diametr = Radius x 2 (example: Radius = 1cm. Diametr = 2cm)
# C circle length = c 2 x P x radius
# P = 3.14
# S = area of the circle. = p * R*2 = p* radius*2
radius = input('Enter the radius: ')
float(radius)
p = pi
float(p)
circle_length = 2*p*float(radius)
y = p*float(radius)*2
float(y)
area_of_the_circle = float(y)*float(radius)*2
print(f"Hello, circle_length is {circle_length} and area_of_the_circle is {area_of_the_circle} .")

# Task #3
usd = 1
uah = 36.42
usd_to_uah = float(usd)*float(uah)
print(f"Current course 1 usd to uah:{float(usd_to_uah)}")











