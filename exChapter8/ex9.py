class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after(self,prev_node_data,data):
        new_node = Node(data)
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node:
            if current_node.data == prev_node_data:
                new_node.next = current_node.next
                return
            current_node = current_node.next
        print("Node with data '{}' not found".format(prev_node_data))

    def delete_node(self,key):
        temp=self.head
        if temp is None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return
        while temp:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return
        prev.next=temp.next
        temp=None

    def print_list(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")

linked_list = LinkedList()
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.print_list()

linked_list.insert_after(5,10)
linked_list.print_list()

linked_list.delete_node(5)
linked_list.print_list()