from datetime import datetime, timedelta


# Реалізуйте біблиотеку з будь-яким функціоналом. Наприклад, створіть функції для арифметичних операцій
# і побудуйте каскад імпортів з декількох packagів. Має бути можливіть імпортувати деякі функції з пакета, але не всі.


class func_one:
    def func_1(self):
        a = 1
        b = 2
        c = a + b
        print(c)


    func_1(self = input('enter any sign: '))

class func_two:
    def func_2(self):
        a = 5
        b = 6
        c = a + b
        print(c)


    func_2(self = input('enter any sign: '))

# Створіть обробку одного будь-якого exception, який не використався як приклад на занятті.
# Виведіть результат в консоль

try:
    ter = open("file", "w")
    ter.write("My test file for exception")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    ter.close()

# Implement a function that adds or subtracts a certain number of days from a given date.
# Accepts as input any date and time (datetime),
#   as well as the value of days (int), and a sign (True or False, which represent + and -).
# Returns a datetime. In this problem, use datetime.timedelta

def my_data(self):
    any_date_a_time = input('enter any date: ')


def add_or_subtract_days():
    date_str = input("Enter a date in the format YYYY-MM-DD: ")

    date = datetime.strptime(date_str, "%Y-%m-%d")

    days = int(input("Enter the number of days: "))

    is_addition = input("Do you want to add or subtract? Enter '+' or '-': ") == "+"

    if is_addition:
        new_date = date + timedelta(days=days)
    else:
        new_date = date - timedelta(days=days)

    return new_date


enter_data = add_or_subtract_days()

# Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні),' \
# ' вираховуючі різницю між наданим значеням і значенням datetime.now(). ' \
# 'Приймає дату та час(datetime),' \
#  повертає два значення: datetime і datetime.timestamp. В цій задачі скористайтесь для конвертації datetime.timestamp.
# Виведіть результат в консоль


def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')

age = calculate_age(birth_date)
print("You are", age, "years old.")
