import threading

# Класс, который содержит два списка
class ListFiller:
    def __init__(self, size):
        self.size = size
        self.char_list = [None] * size  # Список для символов
        self.num_list = [None] * size   # Список для чисел
        self.char_lock = threading.Lock()  # Блокировка для символов
        self.num_lock = threading.Lock()   # Блокировка для чисел

    # Функция для заполнения символами
    def fill_char_list(self):
        for i in range(self.size):
            char = chr(65 + i)  # Преобразуем индекс в символ ('A' = 65)
            with self.char_lock:
                self.char_list[i] = char

    # Функция для заполнения числами
    def fill_num_list(self):
        for i in range(self.size):
            num = i * 10  # Пример числового значения
            with self.num_lock:
                self.num_list[i] = num

    # Функция для запуска потоков
    def fill_lists(self):
        # Создаем потоки
        thread1 = threading.Thread(target=self.fill_char_list)
        thread2 = threading.Thread(target=self.fill_num_list)

        # Запускаем потоки
        thread1.start()
        thread2.start()

        # Ожидаем завершения потоков
        thread1.join()
        thread2.join()

    # Функция для вывода результатов
    def display(self):
        print(f"Список символов: {self.char_list}")
        print(f"Список чисел: {self.num_list}")


def main():
    size = 10  # Размер списков
    filler = ListFiller(size)

    # Запускаем заполнение списков
    filler.fill_lists()

    # Выводим результат
    filler.display()

if __name__ == "__main__":
    main()
