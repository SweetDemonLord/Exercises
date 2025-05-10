class ChainObject:
    def __init__(self, value, next_obj=None):
        self.value = value
        self.next=next_obj
def create_object_chain(num_objects):
    if num_objects <= 0:
        return None

    first_obj=ChainObject(1)
    current_obj=first_obj

    for i in range(2,num_objects):
        new_obj=ChainObject(i**2)
        current_obj.next=new_obj
        current_obj=new_obj

    return first_obj
# Example of use
chain_length=int(input("Enter the length of the chain: "))
first_object=create_object_chain(chain_length)

# Outputting the values of the chain of the object
current_obj=first_object
while current_obj:
    print(current_obj.value, end=" ")
    current_obj=current_obj.next
