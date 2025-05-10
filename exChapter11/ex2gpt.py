import tkinter as tk
from tkinter import PhotoImage

# Создание основного окна
root = tk.Tk()
root.title("Пример программы")
root.geometry("300x250")

# Функция для закрытия окна
def close_window():
    root.quit()

# Функция для смены изображения при наведении
def on_enter(event):
    image_label.config(image=image_hover)  # Сменить на hover изображение

# Функция для возврата исходного изображения, когда курсор покидает область
def on_leave(event):
    image_label.config(image=image_original)  # Сменить на исходное изображение

# Создание кнопки для закрытия окна
button_close = tk.Button(root, text="Закрыть", command=close_window)
button_close.pack(pady=20)

# Загрузка изображений (замените пути на свои изображения)
image_original = PhotoImage(file="D:\\Programming\\Python\\Pictures\\вк\\опа.png")  # Исходное изображение
image_hover = PhotoImage(file="D:\\Programming\\Python\\Pictures\\вк\\vk.png")

# Создание метки с изображением
image_label = tk.Label(root, image=image_original)
image_label.pack(pady=10)

# Привязка событий: при наведении меняем изображение, при уходе возвращаем исходное
image_label.bind("<Enter>", on_enter)
image_label.bind("<Leave>", on_leave)

# Запуск основного цикла обработки событий
root.mainloop()