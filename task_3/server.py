"""
Сервер-программа
"""

import socket
import sys
import json

from common.utils import get_message, send_message

from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT


def process_client_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клиента, проверяет корректность,
    возвращает словарь-ответ для клиента
    :param message:
    :return:
    """
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {RESPONSE: 400, ERROR: 'Bad request'}


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умолчанию.
    :return:
    """

    try:
        if '-p' in sys.argv:
            serv_listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            serv_listen_port = DEFAULT_PORT
        if serv_listen_port < 1024 or serv_listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

        # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            serv_listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            serv_listen_address = ''

    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

        # Готовим сокет

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((serv_listen_address, serv_listen_port))

    # Слушаем порт

    server_socket.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = server_socket.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
