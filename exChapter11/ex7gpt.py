import tkinter as tk

# Функция для изменения фона области
def change_color():
    selected_color = color_var.get()  # Получаем выбранный цвет
    color_area.config(bg=selected_color)  # Меняем фон области

# Создание основного окна
root = tk.Tk()
root.title("Выбор цвета")
root.geometry("300x300")

# Переменная для хранения выбранного цвета
color_var = tk.StringVar(value="white")  # По умолчанию белый цвет

# Текстовая метка
label_prompt = tk.Label(root, text="Выберите цвет:")
label_prompt.pack(pady=10)

# Группа переключателей для выбора цвета
radio_red = tk.Radiobutton(root, text="Красный", value="red", variable=color_var, command=change_color)
radio_red.pack()

radio_green = tk.Radiobutton(root, text="Зеленый", value="green", variable=color_var, command=change_color)
radio_green.pack()

radio_blue = tk.Radiobutton(root, text="Синий", value="blue", variable=color_var, command=change_color)
radio_blue.pack()

radio_yellow = tk.Radiobutton(root, text="Желтый", value="yellow", variable=color_var, command=change_color)
radio_yellow.pack()

# Область для отображения выбранного цвета
color_area = tk.Label(root, text="Область цвета", width=30, height=10, bg=color_var.get())
color_area.pack(pady=20)

# Запуск основного цикла обработки событий
root.mainloop()