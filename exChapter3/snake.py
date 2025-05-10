def fill_snake_matrix(rows, cols):
    # Создаем пустую матрицу
    matrix = [[0] * cols for _ in range(rows)]

    num = 1  # Начинаем заполнять с 1
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        # Заполняем верхнюю строку
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Заполняем правый столбец
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            # Заполняем нижнюю строку
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            # Заполняем левый столбец
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix


# Пример использования
rows = 4
cols = 5

snake_matrix = fill_snake_matrix(rows, cols)

# Вывод матрицы
for row in snake_matrix:
    print(row)
