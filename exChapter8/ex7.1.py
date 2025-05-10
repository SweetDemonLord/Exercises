class MyClass:
    def __init__(self, num_list):
        self.num_list = num_list
def sum_lists(obj1,obj2):
    len1=len(obj1.num_list)
    len2=len(obj2.num_list)

    max_len=max(len1,len2)
    sum_list=[obj1.num_list[i] + obj2.num_list[i] if i < len1 and i < len2
              else (obj1.num_list[i] if i < len1 else obj2.num_list[i])
              for i in range(max_len)]
    return MyClass(sum_list)
obj1=MyClass([1, 2, 3, 4, 5])
obj2=MyClass([10, 20, 30, 40])

result_obj=sum_lists(obj1,obj2)
print(result_obj.num_list)