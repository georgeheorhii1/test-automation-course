import random

# Створіть декоратор, який виводить в консоль ім'я функції, яку було ввикликано. ' \
# Наприклад, створіть пару функцій для аріфметичних операцій додавання і множення.
# При виклику цих функцій має повертатись результат операції і
# виводиться в консоль ім'я функції, яку було ввикликано.

def log_func_name(func):
    def wrapper(*args, **kwargs):
        print(f"The function name is: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_func_name
def addition():
    a = 1
    b = 2
    return a + b

@log_func_name
def multiplication():
    x = 2
    y = 2
    return x * y


multiplication()

addition()


'''Створіть за допомогою list comprehension список, в якому буде 100 елементів,
і кожен із яких буде в границях від 1 до 10(для цього можна скористатись функцією randint із модуля random). 
Порахуйте кількість кожного елемента і виведіть в консоль'''

my_list = [random.randint(1, 10) for _ in range(100)]

for skin in range(1, 11):
    count = my_list.count(skin)
    print(f"Skin {skin}: {count} occurrences")