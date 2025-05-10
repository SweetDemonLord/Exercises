import threading

# Глобальный список
shared_list = [None] * 10  # Изначально список из 10 элементов

# Блокировка для синхронизации доступа к общему списку
list_lock = threading.Lock()


# Функция для заполняния четных индексов буквами
def fill_even_indices():
    for i in range(0, len(shared_list), 2):  # Четные индексы
        with list_lock:
            shared_list[i] = chr(65 + i)  # Присваиваем букву, начиная с 'A'


# Функция для заполняния нечетных индексов числами
def fill_odd_indices():
    for i in range(1, len(shared_list), 2):  # Нечетные индексы
        with list_lock:
            shared_list[i] = i * 10  # Присваиваем число (например, умножаем индекс на 10)


def main():
    # Создаем два потока
    thread1 = threading.Thread(target=fill_even_indices)
    thread2 = threading.Thread(target=fill_odd_indices)

    # Запускаем потоки
    thread1.start()
    thread2.start()

    # Ожидаем завершения потоков
    thread1.join()
    thread2.join()

    # Выводим итоговый список
    print(shared_list)


if __name__ == "__main__":
    main()
