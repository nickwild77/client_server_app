""" Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
в последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных.
"""


WORDS = ['class', 'function', 'method']


def from_str_to_bytes(WORDS: list):
    for word in WORDS:
        word_bytes = bytes(word, 'utf-8')
        print(f"{word_bytes} - {type(word_bytes)} - len {len(word_bytes)}")


from_str_to_bytes(WORDS)
