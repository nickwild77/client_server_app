"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
«сокет», «декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того,
что перед нами файл в неизвестной кодировке.
Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.
"""

from chardet import detect

LINES_LIST = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as file:
    for line in LINES_LIST:
        file.write(f'{line}\n')
file.close()


def encoding_convert():
    with open('test_file.txt', 'rb') as f_obj:
        content_bytes = f_obj.read()
    detected = detect(content_bytes)
    encoding = detected['encoding']
    content_text = content_bytes.decode(encoding)
    with open('test_file.txt', 'w', encoding='utf-8') as f_obj:
        f_obj.write(content_text)


encoding_convert()

with open('test_file.txt', 'r', encoding='utf-8') as file:
    CONTENT = file.read()
print(CONTENT)
