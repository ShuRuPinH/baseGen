import csv
import datetime
import random

import dics as dic
from utils.utilities import randomListItem

def genData(cats: dict, len=10, csv_file_path='example.csv'):
    # Путь к файлу CSV, который мы хотим создать

    # Запонение случайными данными
    result = []
    for i in range(0, len):
        tmp = {}

        for k, v in cats.items():
            print("key ", k)
            if callable(v):
                if k == 'Телефон':
                    tmp[k] = "+7" + str(v(10))
                else:
                    tmp[k] = v(10)

                # print("Переменная является функцией")
            elif isinstance(v, list) or isinstance(v, tuple):
                tmp[k] = randomListItem(v)
                print("Tuple", v[0])
            else:
                tmp[k] = v
                print("Other", v)

        result.append(tmp)

    # Запись данных в CSV-файл
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=cats.keys())

        # Запись заголовков
        writer.writeheader()

        # Запись данных
        for row in result:
            writer.writerow(row)

    print(f'CSV-файл успешно создан: {csv_file_path}')


genData(dic.categoriesFABRICdic, 10, "fab.csv")
genData(dic.categoriesORDERdic, 10, "ord.csv")
