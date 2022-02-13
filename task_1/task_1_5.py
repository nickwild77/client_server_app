"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess
import chardet

RESOURCES = ['yandex.ru', 'youtube.com']

for resource in RESOURCES:
    subprocess_ping = subprocess.Popen(['ping', resource], stdout=subprocess.PIPE)
    for line in subprocess_ping.stdout:
        print(line.decode(chardet.detect(line)['encoding']).encode('utf-8').decode('utf-8'))
