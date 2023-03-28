import json
import re

domains = 'domains.txt'
names = 'names.json'


def read_file(file_name, function):
    string = str(file_name)
    with open(string) as f:
        contents = f.read()
        test = function(contents)
    print(test)


def replace_dots(content):
    return content.replace(".", "")


def get_surnames_from_file(names):
    with open(names, 'r') as f:
        data = json.load(f)
    surnames = [name['user_name'].split()[-1] for name in data]
    print(surnames)


def get_dates_from_file(authors):
    dates = []
    with open(authors, 'r') as file:
        for line in file:
            match = re.search(
                r'\b\d{1,2}(st|nd|rd|th)\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b',
                line)
            if match:
                dates.append({'date': match.group(0)})
        return dates

read_file(domains, replace_dots)

get_surnames_from_file(names)

print(get_dates_from_file('authors.txt'))
