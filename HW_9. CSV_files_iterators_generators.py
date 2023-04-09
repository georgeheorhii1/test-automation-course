import csv


# Task_1
def read_csv_file(file_name):
    
  
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        lines = []
        for line in reader:
            lines.append(','.join(line))
        return lines


def write_to_csv_file(file_name, lines):

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for line in lines:
            writer.writerow(line.split(','))


lines = ['1,2,3', '4,5,6', '7,8,9']
write_to_csv_file('file1.csv', lines)

new_lines = read_csv_file('file1.csv')

new_lines.append('10,11,12')
new_lines.append('13,14,15')

write_to_csv_file('file2.csv', new_lines)


# Создайте функцию, которая возвращает квадраты всех чисел в диапазоне 0 – 100000.
# Должен сработать и не положить ваш компьютер.
def find():
    for i in range(100001):
        yield i ** 2


squares = find()
for i in range(100):
    print(next(squares))
