# Write a Python program to check if a given string is a number using a lambda

check_number = lambda input_string: input_string.replace('.','', 1).isdigit()

input_string = input("enter data: ")
if check_number(input_string):
    print(f"{input_string} it is a number")

else:
    print(f"{input_string} it is not a number")


#  Write a Python program to find a list with maximum and minimum length using lambda.

list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8]

max_lst = max([list_1, list_2], key=lambda x: len(x))
min_lst = min([list_1, list_2], key=lambda x: len(x))

print("List with maximum length:", max_lst)
print("List with minimum length:", min_lst)


