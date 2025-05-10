import tkinter as tk


# Функция для перемещения окружности по углам
def move_circle(event):
    global circle_x, circle_y, circle_id

    # Размеры окна и области рисования
    width, height = canvas.winfo_width(), canvas.winfo_height()

    # Радиус окружности
    radius = 20

    # Перемещение окружности в зависимости от нажатой клавиши
    if event.keysym == "Up":
        circle_x, circle_y = width // 4, height // 4
    elif event.keysym == "Down":
        circle_x, circle_y = width // 4, 3 * height // 4
    elif event.keysym == "Left":
        circle_x, circle_y = width // 4, height // 2
    elif event.keysym == "Right":
        circle_x, circle_y = 3 * width // 4, height // 2

    # Перемещаем окружность, обновляя её координаты
    canvas.coords(circle_id, circle_x - radius, circle_y - radius, circle_x + radius, circle_y + radius)


# Создание основного окна
root = tk.Tk()
root.title("Движущаяся окружность")
root.geometry("400x400")

# Область для рисования
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Начальные координаты центра окружности (по умолчанию в центре окна)
circle_x, circle_y = 200, 200
radius = 20

# Рисуем начальную окружность в центре
circle_id = canvas.create_oval(circle_x - radius, circle_y - radius, circle_x + radius, circle_y + radius, fill="blue")

# Привязка событий клавиатуры
root.bind("<Up>", move_circle)
root.bind("<Down>", move_circle)
root.bind("<Left>", move_circle)
root.bind("<Right>", move_circle)

# Запуск основного цикла обработки событий
root.mainloop()