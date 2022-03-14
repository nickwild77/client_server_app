import logging
import os.path

logger = logging.getLogger('client')

formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(module)-8s - %(message)s")

folder_name = 'log_files'

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

file_name = os.path.join(folder_name, 'client.log')

file_handler = logging.FileHandler(file_name, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования')
    logger.critical('Тестовое сообщение! Критическая ошибка')
    logger.error('Тестовое сообщение! Ошибка')
    logger.debug('Тестовое сообщение! Отладочная информация')
