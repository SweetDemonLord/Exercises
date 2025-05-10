import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # Для работы с изображениями других форматов, кроме .gif и .png


# Функция для отображения изображения выбранного животного
def show_animal_image(event):
    selected_animal = combo_animal.get()  # Получаем выбранное животное
    if selected_animal == "Кошка":
        image_path = "cat.png"
    elif selected_animal == "Собака":
        image_path = "dog.png"
    elif selected_animal == "Лев":
        image_path = "lion.png"
    elif selected_animal == "Тигр":
        image_path = "tiger.png"
    else:
        return

    # Загружаем и отображаем изображение
    try:
        img = Image.open(image_path)
        img = img.resize((250, 250), Image.ANTIALIAS)  # Изменение размера изображения
        img = ImageTk.PhotoImage(img)
        label_image.config(image=img)
        label_image.image = img  # Сохраняем ссылку на изображение, чтобы оно не исчезло
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")


# Создание основного окна
root = tk.Tk()
root.title("Выбор животного")
root.geometry("300x350")

# Список животных
animals = ["Кошка", "Собака", "Лев", "Тигр"]

# Текстовая метка
label_prompt = tk.Label(root, text="Выберите животное:")
label_prompt.pack(pady=10)

# Комбо-виджет для выбора животного
combo_animal = ttk.Combobox(root, values=animals, state="readonly")
combo_animal.pack(pady=10)
combo_animal.bind("<<ComboboxSelected>>", show_animal_image)  # Привязка события выбора

# Место для отображения изображения
label_image = tk.Label(root)
label_image.pack(pady=10)

# Запуск основного цикла обработки событий
root.mainloop()