import threading
import time

# Глобальная переменная для хранения суммы
total_sum = 0
# Блокировка для предотвращения одновременного доступа к общей сумме
sum_lock = threading.Lock()


# Функция для вычисления суммы квадратов в определённом диапазоне
def calculate_squares(start, end):
    global total_sum
    partial_sum = 0
    for i in range(start, end + 1):
        partial_sum += i * i

    # Синхронизация доступа к общей переменной
    with sum_lock:
        total_sum += partial_sum


# Функция для создания и запуска потоков
def main(time_limit=1, max_number=7, num_threads=4):
    start_time = time.time()
    threads = []
    range_size = max_number // num_threads

    # Запуск потоков
    for i in range(num_threads):
        start = i * range_size + 1
        end = (i + 1) * range_size if i != num_threads - 1 else max_number
        thread = threading.Thread(target=calculate_squares, args=(start, end))
        threads.append(thread)
        thread.start()

    # Ограничение по времени
    while time.time() - start_time < time_limit:
        time.sleep(0.1)  # Проверяем, прошло ли достаточно времени

    # Завершаем потоки, ожидая их завершения
    for thread in threads:
        thread.join()

    # Выводим итоговую сумму
    print(f"Общая сумма квадратов: {total_sum}")


if __name__ == "__main__":
    main()
