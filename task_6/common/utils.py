"""
Утилиты
"""

import json

from .variables import MAX_PACKAGE_LENGTH, ENCODING_TYPE


def get_message(sock):
    """
    Функция декодирует принятое сообщение в байтах и возвращает словарь.
    В противном случае возвращает ошибку ValueError
    :param sock:
    :return: response
    :raises ValueError
    """

    encoded_response = sock.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING_TYPE)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    """
    Функция кодирует и отправляет сообщение
    :param sock:
    :param message:
    :return:
    """

    json_massage = json.dumps(message)
    encoded_message = json_massage.encode(ENCODING_TYPE)
    sock.send(encoded_message)
