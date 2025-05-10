class NumberObject:
    def __init__(self,value):
        self.value = value

def create_object_list(num_objects):
    object_list = []
    start_value=1
    for _ in range(num_objects):
        object_list.append(NumberObject(start_value))
        start_value += 2
    return object_list

num_objects=5
object_list=create_object_list(num_objects)

for obj in object_list:
    print(obj.value, end=" ")