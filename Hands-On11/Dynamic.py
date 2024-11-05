class DynamicArray:
    def __init__(self):
        self.size = 0               # Current number of elements in the array
        self.capacity = 1           # Initial capacity of the array
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        """Creates a new array with the given capacity."""
        return [0] * capacity

    def _resize(self, new_capacity):
        """Resizes the internal array to a new capacity."""
        new_array = self._make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, value):
        """Adds an element to the end of the array."""
        if self.size == self.capacity:
            # Double the capacity when the array is full
            self._resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1  # Increment size after appending

    def get(self, index):
        """Returns the element at the specified index."""
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of bounds")

    def set(self, index, value):
        """Sets the element at the specified index to the given value."""
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def remove(self):
        """Removes the last element of the array."""
        if self.size > 0:
            self.size -= 1  # Decrement size after removing
            # Reduce capacity by half if the size is a quarter of the capacity
            if self.size <= self.capacity // 4:
                self._resize(max(1, self.capacity // 2))
        else:
            raise IndexError("Remove from empty array")

    def __str__(self):
        """Returns a string representation of the array."""
        return str([self.array[i] for i in range(self.size)])


# Test the DynamicArray class without intermediate size printing
dynamic_array = DynamicArray()
print("Initial array:", dynamic_array)

# Append elements to the array
dynamic_array.append(10)
dynamic_array.append(20)
dynamic_array.append(30)

# Access elements using get
print("Element at index 0:", dynamic_array.get(0))
print("Element at index 1:", dynamic_array.get(1))
print("Element at index 2:", dynamic_array.get(2))

# Modify elements using set
dynamic_array.set(1, 80)
print("Array after setting index 1 to 80:", dynamic_array)

# Append more elements to trigger resizing
dynamic_array.append(40)
dynamic_array.append(60)

# Remove elements
dynamic_array.remove()
dynamic_array.remove()

# Final state of the array
print("Final array:", dynamic_array)
print("Final array size:", dynamic_array.size)

#OUTPUT
#Initial array: []
#Array size: 0
#Array after appending 10: [10]
#Array size: 1
#Array after appending 20: [10, 20]
#Array size: 2
#Array after appending 30: [10, 20, 30]
#Array size: 3
#Element at index 0: 10
#Element at index 1: 20
#Element at index 2: 30
#Array after setting index 1 to 80: [10, 80, 30]
#Array size: 3
#Array after appending 40: [10, 80, 30, 40]
#Array size: 4
#Array after appending 60: [10, 80, 30, 40, 60]
#Array size: 5
#Array after removing the last element: [10, 80, 30, 40]
#Array size: 4
#Array after removing another element: [10, 80, 30]
#Array size: 3
#Final array: [10, 80, 30]
#Final array size: 3
