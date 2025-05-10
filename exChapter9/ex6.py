class TextClass:
    def __init__(self):
        self._list = ""  # Приватное поле для хранения начальных букв

    @property
    def lst(self):
        """Геттер для получения начальных букв."""
        return self._list

    @lst.setter
    def lst(self, value):
        """Сеттер для присвоения списка строк."""
        if isinstance(value, list):
            # Создаем строку из начальных букв строк в списке
            self._list = ''.join(k[0] for k in value if type(k)==str)
        else:
            raise ValueError("Can't read a field: value must be a list.")

# Пример использования
txt = TextClass()
txt.lst = ["Sos", "odd", "nigger", "yellow"]
print("txt.list =", txt.lst)  # Вывод: txt.list = SOA

# Пример работы с ошибкой
try:
    txt.lst = "Sos"
except ValueError as e:
    print(e)  # Вывод: Can't read a field: value must be a list.
