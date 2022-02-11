"""
4. Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
"""

WORDS = ['разработка', 'администрирование', 'protocol']


def encode_decode(WORDS: list):
    words_to_bytes = [word.encode('utf-8') for word in WORDS]
    [print(f'{word} - {type(word)}') for word in words_to_bytes]

    bytes_to_words = [byte.decode('utf-8') for byte in words_to_bytes]
    [print(f'{byte} - {type(byte)}') for byte in bytes_to_words]


encode_decode(WORDS)
