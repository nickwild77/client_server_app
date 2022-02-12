""" Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
в последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных.
"""

WORDS = ['class', 'function', 'method']


def from_str_to_bytes(WORDS: list):
    for word in WORDS:
        str_byte = eval(f"b'{word}'")
        print(str_byte, type(str_byte), len(str_byte))


from_str_to_bytes(WORDS)
