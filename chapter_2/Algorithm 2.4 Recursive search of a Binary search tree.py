class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
def search(root, key):
    if root is None or root.data == key:
        return root
  
    if root.data < key:
        return search(root.right, key)
    
    return search(root.left, key)

def insert_node(root, val):
    if not root:
        return Node(val)
    if val < root.data:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    return root

root = insert_node(None, 50)
insert_node(root, 30)
insert_node(root, 20)
insert_node(root, 40)
insert_node(root, 70)
insert_node(root, 60)
insert_node(root, 80)


print(search(root, 40).data)