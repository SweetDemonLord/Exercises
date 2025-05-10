import tkinter as tk

# Функция для увеличения размера шрифта
def increase_font_size():
    global font_size
    font_size += 1
    label_text.config(font=("Helvetica", font_size))

# Функция для уменьшения размера шрифта
def decrease_font_size():
    global font_size
    if font_size > 1:
        font_size -= 1
        label_text.config(font=("Helvetica", font_size))

# Создание основного окна
root = tk.Tk()
root.title("Изменение размера шрифта")
root.geometry("600x200")

# Начальный размер шрифта
font_size = 12

# Шаблонный текст
template_text = "Это шаблонный текст. Используйте кнопки для изменения размера шрифта."

# Текстовая метка с шаблонным текстом
label_text = tk.Label(root, text=template_text, font=("Helvetica", font_size))
label_text.pack(pady=20)

# Кнопка для увеличения размера шрифта
button_increase = tk.Button(root, text="Увеличить шрифт", command=increase_font_size)
button_increase.pack(side="left", padx=20)

# Кнопка для уменьшения размера шрифта
button_decrease = tk.Button(root, text="Уменьшить шрифт", command=decrease_font_size)
button_decrease.pack(side="right", padx=20)

# Запуск основного цикла обработки событий
root.mainloop()