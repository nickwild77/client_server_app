import os
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def write_order_to_json(item, quantity, price, buyer, date):
    filename = os.path.join(CURRENT_DIR, '', 'orders.json')

    if os.path.exists(filename):

        with open(filename, encoding="utf-8") as fl:
            data = json.loads(fl.read())

        data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

        with open(filename, "w", encoding="utf-8") as fl:
            json.dump(data, fl, indent=4, separators=(',', ': '), ensure_ascii=False)

        print(f'Данные добавлены в {filename}')

    else:
        print(f'Исходный файл по пути {filename} не найден')


if __name__ == '__main__':
    write_order_to_json('test', '7', '15000', 'John Doe', '01.01.1900')
    write_order_to_json('test 2', '5', '50000', 'Jane Doe', '02.02.2002')
