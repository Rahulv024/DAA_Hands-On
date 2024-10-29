# Refactoring the Red-Black Tree code with modified variable names for clarity and readability.
class RBTreeNode:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left_child = None
        self.right_child = None
        self.parent_node = None

class RedBlackTree:
    def __init__(self):
        self.null_leaf = RBTreeNode(0)
        self.null_leaf.color = 'black'
        self.root_node = self.null_leaf

    # Insert operation
    def insert(self, value):
        new_node = RBTreeNode(value)
        new_node.left_child = self.null_leaf
        new_node.right_child = self.null_leaf
        current_node = self.root_node
        parent_node = None

        while current_node != self.null_leaf:
            parent_node = current_node
            if new_node.value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

        new_node.parent_node = parent_node

        if parent_node is None:
            self.root_node = new_node
        elif new_node.value < parent_node.value:
            parent_node.left_child = new_node
        else:
            parent_node.right_child = new_node

        new_node.color = 'red'
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node.parent_node and node.parent_node.color == 'red':
            if node.parent_node == node.parent_node.parent_node.left_child:
                uncle = node.parent_node.parent_node.right_child
                if uncle.color == 'red':
                    node.parent_node.color = 'black'
                    uncle.color = 'black'
                    node.parent_node.parent_node.color = 'red'
                    node = node.parent_node.parent_node
                else:
                    if node == node.parent_node.right_child:
                        node = node.parent_node
                        self._left_rotate(node)
                    node.parent_node.color = 'black'
                    node.parent_node.parent_node.color = 'red'
                    self._right_rotate(node.parent_node.parent_node)
            else:
                uncle = node.parent_node.parent_node.left_child
                if uncle.color == 'red':
                    node.parent_node.color = 'black'
                    uncle.color = 'black'
                    node.parent_node.parent_node.color = 'red'
                    node = node.parent_node.parent_node
                else:
                    if node == node.parent_node.left_child:
                        node = node.parent_node
                        self._right_rotate(node)
                    node.parent_node.color = 'black'
                    node.parent_node.parent_node.color = 'red'
                    self._left_rotate(node.parent_node.parent_node)

        self.root_node.color = 'black'

    # Left rotation
    def _left_rotate(self, node):
        y = node.right_child
        node.right_child = y.left_child
        if y.left_child != self.null_leaf:
            y.left_child.parent_node = node
        y.parent_node = node.parent_node
        if node.parent_node is None:
            self.root_node = y
        elif node == node.parent_node.left_child:
            node.parent_node.left_child = y
        else:
            node.parent_node.right_child = y
        y.left_child = node
        node.parent_node = y

    # Right rotation
    def _right_rotate(self, node):
        y = node.left_child
        node.left_child = y.right_child
        if y.right_child != self.null_leaf:
            y.right_child.parent_node = node
        y.parent_node = node.parent_node
        if node.parent_node is None:
            self.root_node = y
        elif node == node.parent_node.right_child:
            node.parent_node.right_child = y
        else:
            node.parent_node.left_child = y
        y.right_child = node
        node.parent_node = y

    # Search operation
    def search(self, value):
        current_node = self.root_node
        while current_node != self.null_leaf and value != current_node.value:
            if value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return current_node if current_node != self.null_leaf else None

    # Inorder traversal
    def inorder_traversal(self):
        return self._inorder_recursive(self.root_node, [])

    def _inorder_recursive(self, node, result):
        if node != self.null_leaf:
            self._inorder_recursive(node.left_child, result)
            result.append((node.value, node.color))
            self._inorder_recursive(node.right_child, result)
        return result

# Test the modified Red-Black Tree with updated variable names
rbt = RedBlackTree()
for value in [10, 20, 30, 40, 50, 25]:
    rbt.insert(value)

# Inorder traversal to check if the values are in sorted order with their colors
inorder_result = rbt.inorder_traversal()

# Search tests
search_25 = rbt.search(25).value if rbt.search(25) else "Not found"
search_100 = "Found" if rbt.search(100) else "Not found"

inorder_result, search_25, search_100

# Printing the results to ensure they are displayed for the user.
print("In-Order Traversal with Colors:", inorder_result)
print("Search for 25:", search_25)
print("Search for 100:", search_100)

#OUTPUT
#In-Order Traversal with Colors: [(10, 'black'), (20, 'black'), (25, 'red'), (30, 'black'), (40, 'red'), (50, 'black')]
#Search for 25: 25
#Search for 100: Not found
