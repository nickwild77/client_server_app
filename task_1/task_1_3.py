"""Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""

WORDS = ['attribute', 'класс', 'type']


def catch_not_b_type_word(WORDS: list):
    for word in WORDS:
        try:
            word_bytes = bytes(word, 'utf-8')
            if len(word) != len(word_bytes):
                raise UnicodeError
            print(f"{word_bytes} - {type(word_bytes)} - len {len(word_bytes)}")
        except UnicodeError as exception:
            print(exception)
