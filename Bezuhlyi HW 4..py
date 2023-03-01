# task #1
# students = {
#     "Alex": 5,
#     "Andreas": 7,
#     "Elif": 8,
# }
# average = sum(students.values())/len(students)
# print(average.__round__())

# Task 2
# user ={
#     1: "Ivan",
#     2: "Maria",
#     3: "Segrii",
#
# }
# command = int(input("Add user id (1, 2, 3): "))
#
# print('Hello', {user.get(command, "all")})

# Task 3
# my_list = [1, 2, 3, 3, 4, 4, 4, 5, 5, 7]
# unique_values = set(my_list)
# num_unique_values = len(unique_values)
#
# print("The number of different values in the list is:", num_unique_values)

# task # 4
# list1 = input("Enter the first list of numbers: ").split()
# list2 = input("Enter the second list of numbers: ").split()
# set1 = set(list1)
# set2 = set(list2)
# common_elements = list(set1.intersection(set2))
# common_elements.sort()
# print("Common elements in both lists in ascending order:")
# for element in common_elements:
#     count = min(list1.count(element), list2.count(element))
#     print(f"('{element}', {count}) ", end="")

# Task # 5
# text = input("Enter the text: ")
# words = text.split()
# word_freq = {}
# for word in words:
#     if word in word_freq:
#         word_freq[word] += 1
#     else:
#         word_freq[word] = 1
# print("Word frequencies:")
# for word, freq in word_freq.items():
#     print(f"('{word}', {freq})")
