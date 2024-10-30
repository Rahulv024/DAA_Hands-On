# Refactoring the Binary Search Tree code with modified variable names for clarity and readability.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        if self.root_node is None:
            self.root_node = TreeNode(data)
        else:
            self._insert_recursive(self.root_node, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(data)
            else:
                self._insert_recursive(current_node.left_child, data)
        else:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(data)
            else:
                self._insert_recursive(current_node.right_child, data)

    def search(self, data):
        return self._search_recursive(self.root_node, data)

    def _search_recursive(self, current_node, data):
        if current_node is None or current_node.data == data:
            return current_node
        if data < current_node.data:
            return self._search_recursive(current_node.left_child, data)
        return self._search_recursive(current_node.right_child, data)

    def delete(self, data):
        self.root_node = self._delete_recursive(self.root_node, data)

    def _delete_recursive(self, current_node, data):
        if current_node is None:
            return current_node

        if data < current_node.data:
            current_node.left_child = self._delete_recursive(current_node.left_child, data)
        elif data > current_node.data:
            current_node.right_child = self._delete_recursive(current_node.right_child, data)
        else:
            if current_node.left_child is None:
                return current_node.right_child
            elif current_node.right_child is None:
                return current_node.left_child

            temp = self._find_min_value_node(current_node.right_child)
            current_node.data = temp.data
            current_node.right_child = self._delete_recursive(current_node.right_child, temp.data)
        return current_node

    def _find_min_value_node(self, node):
        current = node
        while current.left_child is not None:
            current = current.left_child
        return current

    def inorder_traversal(self):
        return self._inorder_recursive(self.root_node, [])

    def _inorder_recursive(self, current_node, result):
        if current_node is not None:
            self._inorder_recursive(current_node.left_child, result)
            result.append(current_node.data)
            self._inorder_recursive(current_node.right_child, result)
        return result

# Test the modified Binary Search Tree with the updated variable names
bst = BinarySearchTree()
for value in [50, 30, 20, 40, 70, 60, 10]:
    bst.insert(value)

# Perform inorder traversal before and after deletion operations
initial_inorder = bst.inorder_traversal()

# Deletion tests
bst.delete(20)
inorder_after_delete_20 = bst.inorder_traversal()

bst.delete(30)
inorder_after_delete_30 = bst.inorder_traversal()

bst.delete(50)
inorder_after_delete_50 = bst.inorder_traversal()

initial_inorder, inorder_after_delete_20, inorder_after_delete_30, inorder_after_delete_50

# Printing the results to ensure they are displayed for the user.
print("In-Order Traversal (Initial):", initial_inorder)
print("In-Order Traversal after Deleting 20:", inorder_after_delete_20)
print("In-Order Traversal after Deleting 30:", inorder_after_delete_30)
print("In-Order Traversal after Deleting 50:", inorder_after_delete_50)

#OUTPUT
#In-Order Traversal (Initial): [10, 20, 30, 40, 50, 60, 70]
#In-Order Traversal after Deleting 20: [10, 30, 40, 50, 60, 70]
#In-Order Traversal after Deleting 30: [10, 40, 50, 60, 70]
#In-Order Traversal after Deleting 50: [10, 40, 60, 70]
