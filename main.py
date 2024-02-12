import time


def real_time_timer():
    start_time = time.time()  # Получаем текущее время в секундах с начала эпохи (обычно 1 января 1970 года)

    while True:
        current_time = time.time()  # Получаем текущее время
        elapsed_time = current_time - start_time  # Вычисляем прошедшее время

        # Преобразуем прошедшее время в формат часы:минуты:секунды
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Выводим время на экран
        print(f"Прошло времени: {int(hours)}:{int(minutes)}:{int(seconds)}", end='\r')

        time.sleep(1)  # Ждем 1 секунду перед обновлением времени


if __name__ == "__main__":
    real_time_timer()
