class Node:
    def __init__(self, data, next_node=-1):
        self.data = data
        self.next = next_node  # Simulates the pointer to the next node

class FixedSizeSinglyLinkedList:
    def __init__(self, max_size):
        self.nodes = [None] * max_size  # Fixed size array for the list
        self.head = -1  # Head of the list
        self.max_size = max_size
        self.next_available = 0  # Points to the next available index in the array

    def insert_end(self, data):
        if self.next_available == self.max_size:
            raise Exception("List is full!")
        
        new_node = Node(data, -1)
        if self.head == -1:
            self.head = self.next_available
        else:
            current = self.head
            while self.nodes[current].next != -1:
                current = self.nodes[current].next
            self.nodes[current].next = self.next_available
        
        self.nodes[self.next_available] = new_node
        self.next_available += 1

    def delete_first(self):
        if self.head == -1:
            raise Exception("List is empty!")
        
        value = self.nodes[self.head].data
        self.head = self.nodes[self.head].next
        return value

    def delete_last(self):
        if self.head == -1:
            raise Exception("List is empty!")
        
        if self.nodes[self.head].next == -1:
            value = self.nodes[self.head].data
            self.head = -1
            return value
        
        current = self.head
        while self.nodes[self.nodes[current].next].next != -1:
            current = self.nodes[current].next
        
        last_value = self.nodes[self.nodes[current].next].data
        self.nodes[current].next = -1
        return last_value

    def display_list(self):
        if self.head == -1:
            print("List is empty")
        else:
            current = self.head
            values = []
            while current != -1:
                values.append(self.nodes[current].data)
                current = self.nodes[current].next
            print("List contents:", values)

# Example
linked_list = FixedSizeSinglyLinkedList(5)
linked_list.insert_end(10)
linked_list.insert_end(20)
linked_list.insert_end(30)
linked_list.insert_end(40)
linked_list.insert_end(50)
linked_list.display_list()
print("Deleted from start:", linked_list.delete_first())
print("Deleted from end:", linked_list.delete_last())
linked_list.display_list()
