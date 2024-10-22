class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def delete(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length


class HashTable:
    def __init__(self, size=8, hash_func=None):
        self.size = size
        self.buckets = [DoublyLinkedList() for _ in range(self.size)]
        self.num_elements = 0
        self.load_factor = 0.75  # Grow when more than 75% full
        self.shrink_factor = 0.25  # Shrink when less than 25% full
        self.hash_func = hash_func if hash_func else self.default_hash_func

    def default_hash_func(self, key):
        # Multiplication and division method for the hash function
        A = (5**0.5 - 1) / 2  # Multiplier for the multiplication method
        return int((self.size * ((key * A) % 1)) + (key % self.size)) % self.size

    def rehash(self, new_size):
        old_buckets = self.buckets
        self.size = new_size
        self.buckets = [DoublyLinkedList() for _ in range(self.size)]
        self.num_elements = 0
        for bucket in old_buckets:
            current = bucket.head
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        bucket_index = self.hash_func(key)
        bucket = self.buckets[bucket_index]
        node = bucket.find(key)
        if node:
            node.value = value  # Update the value if the key already exists
        else:
            bucket.insert(key, value)
            self.num_elements += 1

        
        if self.num_elements / self.size > self.load_factor:
            self.rehash(self.size * 2)

    def delete(self, key):
        bucket_index = self.hash_func(key)
        bucket = self.buckets[bucket_index]
        if bucket.delete(key):
            print(f"Removing key: {key}")
            self.num_elements -= 1

        
        if self.num_elements / self.size < self.shrink_factor and self.size > 8:
            self.rehash(self.size // 2)

    def get(self, key):
        bucket_index = self.hash_func(key)
        bucket = self.buckets[bucket_index]
        node = bucket.find(key)
        if node:
            return node.value
        return None

    def __len__(self):
        return self.num_elements

    def display(self):
        for i, bucket in enumerate(self.buckets):
            current = bucket.head
            print(f"Bucket {i}:", end=" ")
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")


# Example 
hash_table = HashTable()

# Insert key-value pairs
hash_table.insert(10, 24)
hash_table.insert(20, 18)
hash_table.insert(30, 7)
hash_table.insert(40, 45)

# Display the hash table
hash_table.display()

# Get a value
print("Value for key 30:", hash_table.get(30))

# Delete a key
hash_table.delete(30)

# Display the hash table after deletion
hash_table.display()



#OUTPUT
#Bucket 0: None
#Bucket 1: None
#Bucket 2: (30: 7) -> None
#Bucket 3: (10: 24) -> None
#Bucket 4: None
#Bucket 5: (40: 45) -> None
#Bucket 6: (20: 18) -> None
#Bucket 7: None
#Value for key 30: 7
#Removing key: 30
#Bucket 0: None
#Bucket 1: None
#Bucket 2: None
#Bucket 3: (10: 24) -> None
#Bucket 4: None
#Bucket 5: (40: 45) -> None
#Bucket 6: (20: 18) -> None
#Bucket 7: None
