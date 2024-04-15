import threading
import logging


# Налаштування логування
def get_log(log_level):
    local_logger = logging.getLogger("user_data")
    local_logger.setLevel(log_level)

    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(log_level)

    local_logger.addHandler(file_handler)

    return local_logger


# 1й потік закінчує свою роботу, якщо data == 1000
def increase_data():
    global data
    while True:
        with lock:
            data += 1
            logger.debug("Tread 1: data = %d", data)
            if data == 1000:
                break


# 2й потік закінчує свою роботу, якщо data == -1000
def decrease_data():
    global data
    while True:
        with lock:
            data -= 1
            logger.debug("Tread 2: data = %d", data)
            if data == -1000:
                break


data = 0
# Створюємо об'єкт блокування для забезпечення потокобезпеки при зміні значення data
lock = threading.Lock()

# Отримуємо об'єкта логгера
logger = get_log(logging.DEBUG)

# Створюємо потоки
thread1 = threading.Thread(target=increase_data)
thread2 = threading.Thread(target=decrease_data)

# Запускаємо потоки
thread1.start()
thread2.start()

# Очікуємо завершення обох потоків
thread1.join()
thread2.join()

logger.info("Completed")
