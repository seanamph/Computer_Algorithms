class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.left_size = 0
        self.right_size = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
            cur_node.left_size += 1
        else:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
            cur_node.right_size += 1
            
    def find_rank(self, value):
        return self._find_rank(value, self.root)
    
    def _find_rank(self, value, cur_node):
        if cur_node is None:
            return -1
        elif cur_node.value == value:
            return cur_node.left_size + 1
        elif value < cur_node.value:
            return self._find_rank(value, cur_node.left)
        else:
            right_rank = self._find_rank(value, cur_node.right)
            if right_rank == -1:
                return -1
            else:
                return cur_node.left_size + 1 + right_rank


tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(9)

print(tree.find_rank(5))   # Output: 2
print(tree.find_rank(1))   # Output: 0
print(tree.find_rank(9))   # Output: 4
print(tree.find_rank(4))   # Output: 2