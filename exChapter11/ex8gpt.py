import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
from PIL import Image, ImageTk


# Функция для отображения изображения выбранного животного
def show_animal_image(animal):
    try:
        # Путь к изображению в зависимости от выбранного животного
        if animal == "Кошка":
            image_path = "cat.png"
        elif animal == "Собака":
            image_path = "dog.png"
        elif animal == "Лев":
            image_path = "lion.png"
        elif animal == "Тигр":
            image_path = "tiger.png"
        else:
            messagebox.showerror("Ошибка", "Изображение не найдено!")
            return

        # Загружаем изображение
        img = Image.open(image_path)
        img = img.resize((250, 250), Image.ANTIALIAS)  # Изменяем размер изображения
        img = ImageTk.PhotoImage(img)

        # Отображаем изображение в метке
        label_image.config(image=img)
        label_image.image = img  # Сохраняем ссылку на изображение
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")


# Создание основного окна
root = tk.Tk()
root.title("Выбор животного")
root.geometry("400x400")

# Текстовая метка
label_prompt = tk.Label(root, text="Выберите животное из меню:")
label_prompt.pack(pady=10)

# Место для отображения изображения
label_image = tk.Label(root)
label_image.pack(pady=20)

# Создание главного меню
menu = Menu(root)
root.config(menu=menu)

# Подменю "Животные"
animal_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Животные", menu=animal_menu)

# Добавление пунктов в подменю для выбора животного
animal_menu.add_command(label="Кошка", command=lambda: show_animal_image("Кошка"))
animal_menu.add_command(label="Собака", command=lambda: show_animal_image("Собака"))
animal_menu.add_command(label="Лев", command=lambda: show_animal_image("Лев"))
animal_menu.add_command(label="Тигр", command=lambda: show_animal_image("Тигр"))

# Запуск основного цикла обработки событий
root.mainloop()