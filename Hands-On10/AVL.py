# Refactoring the AVL Tree code with modified variable names for clarity and readability.
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1  # New node is initially added at leaf

class AVLTree:
    def __init__(self):
        self.root_node = None  # Initialize the root node as None

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left_child) - self._get_height(node.right_child) if node else 0

    def _right_rotate(self, y):
        x = y.left_child
        T2 = x.right_child

        # Perform rotation
        x.right_child = y
        y.left_child = T2

        # Update heights
        y.height = max(self._get_height(y.left_child), self._get_height(y.right_child)) + 1
        x.height = max(self._get_height(x.left_child), self._get_height(x.right_child)) + 1

        return x

    def _left_rotate(self, x):
        y = x.right_child
        T2 = y.left_child

        # Perform rotation
        y.left_child = x
        x.right_child = T2

        # Update heights
        x.height = max(self._get_height(x.left_child), self._get_height(x.right_child)) + 1
        y.height = max(self._get_height(y.left_child), self._get_height(y.right_child)) + 1

        return y

    def _insert(self, node, data):
        if not node:
            return AVLNode(data)
        elif data < node.data:
            node.left_child = self._insert(node.left_child, data)
        else:
            node.right_child = self._insert(node.right_child, data)

        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))
        balance = self._get_balance(node)

        # Balance cases
        if balance > 1 and data < node.left_child.data:
            return self._right_rotate(node)
        if balance < -1 and data > node.right_child.data:
            return self._left_rotate(node)
        if balance > 1 and data > node.left_child.data:
            node.left_child = self._left_rotate(node.left_child)
            return self._right_rotate(node)
        if balance < -1 and data < node.right_child.data:
            node.right_child = self._right_rotate(node.right_child)
            return self._left_rotate(node)

        return node

    def insert(self, data):
        self.root_node = self._insert(self.root_node, data)

    def _min_value_node(self, node):
        current = node
        while current.left_child:
            current = current.left_child
        return current

    def _delete(self, node, data):
        if not node:
            return node

        elif data < node.data:
            node.left_child = self._delete(node.left_child, data)
        elif data > node.data:
            node.right_child = self._delete(node.right_child, data)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            temp = self._min_value_node(node.right_child)
            node.data = temp.data
            node.right_child = self._delete(node.right_child, temp.data)

        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))
        balance = self._get_balance(node)

        # Balance cases
        if balance > 1 and self._get_balance(node.left_child) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._get_balance(node.left_child) < 0:
            node.left_child = self._left_rotate(node.left_child)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right_child) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._get_balance(node.right_child) > 0:
            node.right_child = self._right_rotate(node.right_child)
            return self._left_rotate(node)

        return node

    def delete(self, data):
        self.root_node = self._delete(self.root_node, data)

    def search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search(node.left_child, data)
        return self.search(node.right_child, data)

    def inorder_traversal(self, node):
        return self._inorder_recursive(node, [])

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left_child, result)
            result.append(node.data)
            self._inorder_recursive(node.right_child, result)
        return result

# Test AVL Tree with refactored variable names
avl_tree = AVLTree()

# Insert nodes
for value in [10, 20, 30, 40, 50, 25]:
    avl_tree.insert(value)

# Inorder traversal to check the sorted structure of the AVL tree
inorder_result = avl_tree.inorder_traversal(avl_tree.root_node)

# Search for nodes
search_30 = "Found" if avl_tree.search(avl_tree.root_node, 30) else "Not found"
search_100 = "Found" if avl_tree.search(avl_tree.root_node, 100) else "Not found"

# Delete nodes and print inorder traversal after each deletion
avl_tree.delete(50)
inorder_after_delete_50 = avl_tree.inorder_traversal(avl_tree.root_node)

avl_tree.delete(30)
inorder_after_delete_30 = avl_tree.inorder_traversal(avl_tree.root_node)

# Display the results
print("Inorder Traversal:", inorder_result)
print("Search for 30:", search_30)
print("Search for 100:", search_100)
print("Inorder Traversal after Deleting 50:", inorder_after_delete_50)
print("Inorder Traversal after Deleting 30:", inorder_after_delete_30)

#OUTPUT
#Inorder Traversal: [10, 20, 25, 30, 40, 50]
#Search for 30: Found
#Search for 100: Not found
#Inorder Traversal after Deleting 50: [10, 20, 25, 30, 40]
#Inorder Traversal after Deleting 30: [10, 20, 25, 40]
