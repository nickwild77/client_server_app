import csv
import re
import chardet
import pathlib
from pathlib import Path

path_files = Path(pathlib.Path.cwd())


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    manufacturer = 'Изготовитель системы'
    os_name = 'Название ОС'
    product_code = 'Код продукта'
    type_of_system = 'Тип системы'

    for i in range(1, 4):
        with open(f'{path_files}/info_{i}.txt', 'rb') as f_obj:
            rawdata = f_obj.read()
            result = chardet.detect(rawdata)
            file = rawdata.decode(result['encoding'])

        os_prod_get = re.compile(fr'{manufacturer}:\s*\S*')
        os_prod_list.append(os_prod_get.findall(file)[0].split()[2])

        os_name_reg = re.compile(r'Windows\s*\S*')
        os_name_list.append(os_name_reg.findall(file)[0])

        os_code_reg = re.compile(fr'{product_code}:\s*\S*')
        os_code_list.append(os_code_reg.findall(file)[0].split()[2])

        os_type_reg = re.compile(fr'{type_of_system}:\s*\S*')
        os_type_list.append(os_type_reg.findall(file)[0].split()[2])

    headers = [manufacturer, os_name, product_code, type_of_system]
    main_data.append(headers)

    received_data = [os_prod_list, os_name_list, os_code_list, os_type_list]

    for i in range(len(received_data[0])):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    return main_data


def write_to_csv(file_name):
    main_data = get_data()
    with open(file_name, 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for row in main_data:
            write.writerow(row)

    print(f'Данные успешно сохранены в {file_name}')


write_to_csv('result.csv')
