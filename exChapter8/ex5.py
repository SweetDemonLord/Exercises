class CustomObject:
    def __init__(self, dc):
        for key, value in dc.items():
            if type(value)==int and not key.startswith("__"):  # Условие для добавления только целочисленных значений без системных полей
                self.__dict__[key] = value

def create_custom_object(obj):
    original_dict = obj.__dict__
    return CustomObject(original_dict)

# Пример использования
class ExampleObject:
    def __init__(self):
        self.name = "Insaf"
        self.age = 23
        self.__private_info = "I like sleepyhead"
        self.number = 777

# Создаем объект класса ExampleObject
original_obj = ExampleObject()

# Создаем новый объект, содержащий только целочисленные поля из original_obj
new_obj = create_custom_object(original_obj)

# Выводим атрибуты нового объекта
print(new_obj.__dict__)