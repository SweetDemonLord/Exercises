import tkinter as tk

def update_label(*args):
    # Дублируем текст из поля ввода в метку
    label.config(text=entry.get())

def clear_fields():
    # Очищаем поле ввода и метку
    entry.delete(0, tk.END)
    label.config(text="")

def close_window():
    # Закрываем окно
    root.destroy()

# Создаем главное окно
root = tk.Tk()
root.title("Пример с кнопками")

# Создаем поле ввода
entry = tk.Entry(root)
entry.pack(padx=30,pady=30)

# Создаем метку
label = tk.Label(root, text="")
label.pack(pady=10)

# При изменении текста в поле ввода обновляем метку
entry.bind('<KeyRelease>', update_label)

# Создаем кнопку для очистки
button_clear = tk.Button(root, text="Очистить", command=clear_fields)
button_clear.pack(pady=5)

# Создаем кнопку для закрытия окна
button_close = tk.Button(root, text="Закрыть", command=close_window)
button_close.pack(pady=5)

# Запускаем основной цикл программы
root.mainloop()