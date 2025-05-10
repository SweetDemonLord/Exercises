import tkinter as tk
from tkinter import messagebox

# Функция для вычисления выражения
def evaluate_expression():
    expression = entry.get()  # Получаем выражение из поля ввода
    try:
        result = eval(expression)  # Вычисляем результат с помощью eval
        label_result.config(text=f"Результат: {result}")  # Отображаем результат
    except Exception as e:
        messagebox.showerror("Ошибка", f"Некорректное выражение: {e}")  # Обработка ошибок

# Создание основного окна
root = tk.Tk()
root.title("Вычисление выражения")
root.geometry("400x200")

# Текстовая метка
label_prompt = tk.Label(root, text="Введите выражение:")
label_prompt.pack(pady=10)

# Поле ввода для выражения
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Кнопка для вычисления выражения
button_calculate = tk.Button(root, text="Вычислить", command=evaluate_expression)
button_calculate.pack(pady=10)

# Метка для отображения результата
label_result = tk.Label(root, text="Результат:")
label_result.pack(pady=10)

# Запуск основного цикла обработки событий
root.mainloop()