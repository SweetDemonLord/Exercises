import tkinter as tk
from tkinter import messagebox
import datetime

# Функция для вычисления года рождения
def calculate_birth_year():
    try:
        age = int(entry_age.get())  # Получаем возраст из поля ввода
        current_year = datetime.datetime.now().year  # Текущий год
        birth_year = current_year - age  # Вычисляем год рождения
        messagebox.showinfo("Год рождения", f"Ваш год рождения: {birth_year}")  # Показываем результат
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректный возраст.")  # Обработка ошибок

# Создание основного окна
root = tk.Tk()
root.title("Вычисление года рождения")
root.geometry("300x150")

# Текстовое описание
label_prompt = tk.Label(root, text="Введите ваш возраст:")
label_prompt.pack(pady=10)

# Поле ввода для возраста
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

# Кнопка для вычисления года рождения
button_calculate = tk.Button(root, text="Вычислить", command=calculate_birth_year)
button_calculate.pack(pady=10)

# Запуск основного цикла обработки событий
root.mainloop()