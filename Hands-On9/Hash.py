class HashTable:
    def __init__(self, initial_size=8):
        self.size = initial_size
        self.count = 0
        self.keys = [None] * initial_size
        self.values = [None] * initial_size

    def insert(self, key, value):
        if self.is_full():
            self.resize(self.size * 2)

        index = self.hash_function(key)

        while self.keys[index] is not None and self.keys[index] != key:
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value
        self.count += 1

    def remove(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Print the key value pair before removal
                old_value = self.values[index]
                print(f"Removing key-value pair: ({self.keys[index]}, {old_value})")

                # Remove the key value pair
                self.keys[index] = None
                self.values[index] = None
                self.count -= 1

                # Only resize if needed
                if self.count <= self.size // 4 and self.size > 8:
                    self.resize(self.size // 2)
                return
            index = (index + 1) % self.size

    def search(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size

        return None  # Key not found

    def hash_function(self, key):
        return key % self.size

    def is_full(self):
        return self.count >= self.size // 2

    def is_empty(self):
        return self.count == 0

    def resize(self, new_size):
        old_keys = self.keys
        old_values = self.values

        self.size = new_size
        self.keys = [None] * new_size
        self.values = [None] * new_size
        self.count = 0

        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.insert(old_keys[i], old_values[i])

# Example usage
ht = HashTable()
ht.insert(10, 111)
ht.insert(20, 222)
ht.insert(30, 333)
ht.insert(40, 444)
ht.insert(50, 555)
ht.insert(60, 666)

# Display and search for the value of key 30
print("Value for key 30:", ht.search(30))  # Output: 333

# Remove the key-value pair for key 30
ht.remove(30)

# Search for key 30 after removal
print("Value for key 30 after removal:", ht.search(30))  # Output: None

# Retrieve other values
print(ht.search(10))  # Output: 111
print(ht.search(20))  # Output: 222
print(ht.search(30))  # Output: None
print(ht.search(40))  # Output: 444
print(ht.search(50))  # Output: 555
print(ht.search(60))  # Output: 666
