class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_binary_tree(depth, current_depth=1):
    if current_depth > depth:
        return None
    node=Node(current_depth)
    node.left = build_binary_tree(depth, current_depth+1)
    node.right = build_binary_tree(depth, current_depth+1)
    return node
def print_tree(node,level=0,label='root'):
    if node is not None:
        print(" " * level + f"{label}:{node.data}")
        print_tree(node.left,level+1,"left")
        print_tree(node.right,level+1,"right")
depth=4
root=build_binary_tree(depth)
print_tree(root)
