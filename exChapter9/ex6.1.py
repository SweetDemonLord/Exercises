class MyCustomClass:
    def __init__(self):
        self._my_list = []  # Приватное поле для хранения списка

    @property
    def my_list(self):
        """Геттер для получения начальных букв строк в списке."""
        return ''.join(item[0] for item in self._my_list if isinstance(item, str))

    @my_list.setter
    def my_list(self, value):
        """Сеттер для присвоения только списка строк."""
        if isinstance(value, list) and all(isinstance(item, str) for item in value):
            self._my_list = [item for item in value]
        else:
            raise ValueError("Значение должно быть списком строк.")

# Пример использования
obj = MyCustomClass()
obj.my_list = ["apple", "banana", "cherry"]
print(obj.my_list)  # Вывод: ABC

obj.my_list = ["dog", "cat", "elephant"]
print(obj.my_list)  # Вывод: DCE

# Пример работы с ошибкой
try:
    obj.my_list = ["hello", 123, "world"]
except ValueError as e:
    print(e)  # Вывод: Значение должно быть списком строк.
