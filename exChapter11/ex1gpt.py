import tkinter as tk
from tkinter import PhotoImage

# Создание основного окна
root = tk.Tk()
root.title("Пример программы")
root.geometry("300x250")

# Функция для закрытия окна
def close_window():
    root.quit()

# Создание кнопки, которая вызывает функцию close_window
button_close = tk.Button(root, text="Закрыть", command=close_window)
button_close.pack(pady=20)

# Добавление текстовой метки
label_text = tk.Label(root, text="Текстовая метка")
label_text.pack()

# Загрузка изображения (замените 'your_image.png' на путь к своему изображению)
try:
    image = PhotoImage(file="D:\\Programming\\Python\\Pictures\\2OmarKhayyam.png")  # Путь к изображению
    label_image = tk.Label(root, image=image)
    label_image.pack(pady=10)
except Exception as e:
    print("Ошибка загрузки изображения:", e)

# Запуск основного цикла обработки событий
root.mainloop()