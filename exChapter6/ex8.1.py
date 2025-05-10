def geometric_progression_sum(a, r, n):
    if n == 0:
        return 0
    else:
        return a + geometric_progression_sum(a * r, r, n - 1)

# Ввод данных пользователем
a = 1  # Первый член геометрической прогрессии
r = 2  # Заданный множитель
n = 5  # Количество членов в прогрессии

# Вычисление суммы геометрической прогрессии
result = geometric_progression_sum(a, r, n)
print(f"Сумма геометрической прогрессии: {result}")