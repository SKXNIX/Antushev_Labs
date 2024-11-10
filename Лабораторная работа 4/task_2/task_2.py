# TODO импортировать необходимые молули
import os
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r") as input_file:
        data = csv.DictReader(input_file, delimiter=",", quotechar='\n')
        data_list = list()
        for row in data:
            data_list.append(row)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w') as output_file:
        json.dump(data_list, output_file, indent=4, ensure_ascii=True)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")