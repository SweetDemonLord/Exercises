import threading

# Класс для создания и заполнения двумерного списка
class TwoDimensionalList:
    def __init__(self, rows, cols):
        self.rows = rows  # Количество строк
        self.cols = cols  # Количество столбцов
        self.matrix = [[None] * cols for _ in range(rows)]  # Инициализация двумерного списка
        self.locks = [threading.Lock() for _ in range(rows)]  # Блокировки для каждой строки

    # Функция для заполнения одной строки
    def fill_row(self, row):
        for col in range(self.cols):
            # Пример заполнения: ставим произведение индексов строки и столбца
            value = row * 10 + col
            with self.locks[row]:  # Блокировка строки
                self.matrix[row][col] = value

    # Функция для запуска потоков и заполнения всего двумерного списка
    def fill_matrix(self):
        threads = []
        for row in range(self.rows):
            # Создаем поток для заполнения каждой строки
            thread = threading.Thread(target=self.fill_row, args=(row,))
            threads.append(thread)
            thread.start()

        # Ожидаем завершения всех потоков
        for thread in threads:
            thread.join()

    # Функция для вывода двумерного списка
    def display(self):
        for row in self.matrix:
            print(row)


def main():
    rows = 5  # Количество строк
    cols = 6  # Количество столбцов
    matrix_filler = TwoDimensionalList(rows, cols)

    # Заполняем двумерный список
    matrix_filler.fill_matrix()

    # Выводим результат
    matrix_filler.display()


if __name__ == "__main__":
    main()
