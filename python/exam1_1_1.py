class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.left_size = 0  # New attribute for left subtree size


class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert_new_node(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insert_by_recursion(value, self.root)
    def insert_by_recursion(self, value, cur_node):
        cur_node.left_size += 1  # Increment left subtree size
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self.insert_by_recursion(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self.insert_by_recursion(value, cur_node.right_child)
    def print_tree(self):
        if self.root != None:
            self.print_node_by_recursion(self.root)
    def print_node_by_recursion(self, cur_node):
        if cur_node != None:
            self.print_node_by_recursion(cur_node.left_child)
            print(cur_node.value)
            self.print_node_by_recursion(cur_node.right_child)

    def fill_tree(self, num_elems=10, max_value=100):
        input_array = [55, 41, 71, 54, 93, 43, 14, 73, 5, 15]
        for cur_elem in input_array:
            self.insert_new_node(cur_elem)


bst_tree = BinarySearchTree()
bst_tree.fill_tree()
bst_tree.print_tree()
