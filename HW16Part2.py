#2 завдання. скористайтесь pytest. напишіть функцію, яка додає в csv один рядок.
#Напишіть функцію, яка видаляє з csv один рядок. напишіть два тести,
#які перевіряють відповідно чи додався рядок і чи він видалився. в якості перевірного csv можете скористатись
#доданим до завдання файлом або будь-яким іншим.

import csv


def add_line_to_csv(line):
    with open('example.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(line)


def delete_row_from_csv(index):
    rows = []
    with open('example.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    with open('example.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i, row in enumerate(rows):
            if i != index:
                writer.writerow(row)


def test_add_line_to_csv(tmpdir):
    line = ['1', 'John', 'Doe']
    add_line_to_csv(line)
    with open('example.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    assert len(rows) == 1
    assert rows[0] == line


def test_delete_row_from_csv(tmpdir):
    lines = [['1', 'John', 'Doe'], ['2', 'Jane', 'Doe'], ['3', 'Bob', 'Smith']]
    with open('example.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            writer.writerow(line)
    delete_row_from_csv(1)
    with open('example.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    assert len(rows) == 2
    assert rows == [lines[0], lines[2]]
