"""1 завдання. Напишіть адаптер, який конвертує json в csv. тобто робить зворотню конвертацію від тієї,
що ми реалізували на уроці. Приклад з уроку, а також json і csv додано, формат запису даних той самий.


"""

import csv
import json


class JSONtoCSVConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            if isinstance(data, dict):
                data = [data]
            self.__lines = data

    def write_file(self, filename: str):
        if not self.__lines:
            return
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = self.__lines[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.__lines)
            self.cleanup()

    def cleanup(self):
        self.__lines = []


converter = JSONtoCSVConverter()
converter.read_file('example.json')
converter.write_file('example.csv')


