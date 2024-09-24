class PriorityHeap:
    def __init__(self):
        self.int_items = []  # Heap to store integer values
        self.float_items = []  # Heap to store float values

    def get_parent(self, idx):
        return (idx - 1) >> 1

    def get_left_child(self, idx):
        return (idx << 1) + 1

    def get_right_child(self, idx):
        return (idx << 1) + 2

    def add(self, value):
        if isinstance(value, int):
            self.int_items.append(value)  # Insert integer into int_items
            self._move_up(self.int_items, len(self.int_items) - 1)
        elif isinstance(value, float):
            self.float_items.append(value)  # Insert float into float_items
            self._move_up(self.float_items, len(self.float_items) - 1)

    def _move_up(self, heap, idx):
        while idx > 0 and heap[idx] < heap[self.get_parent(idx)]:
            parent_idx = self.get_parent(idx)
            heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
            idx = parent_idx

    def _move_down(self, heap, idx):
        smallest = idx
        left = self.get_left_child(idx)
        right = self.get_right_child(idx)

        if left < len(heap) and heap[left] < heap[smallest]:
            smallest = left

        if right < len(heap) and heap[right] < heap[smallest]:
            smallest = right

        if smallest != idx:
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            self._move_down(heap, smallest)

    def build_heap(self, data_list):
        for item in data_list:
            self.add(item)

    def _remove_min(self, heap):
        min_value = heap[0]
        last_value = heap.pop()

        if heap:
            heap[0] = last_value
            self._move_down(heap, 0)

        return min_value

    # Remove the smallest value from the integer heap
    def remove_min_int(self):
        if not self.int_items:
            raise IndexError("Integer heap is empty")
        return self._remove_min(self.int_items)

    # Remove the smallest value from the float heap
    def remove_min_float(self):
        if not self.float_items:
            raise IndexError("Float heap is empty")
        return self._remove_min(self.float_items)

    # Display the integer and float heaps
    def print_items(self):
        print(f"Integer values: {self.int_items}")
        print(f"Float values: {self.float_items}")


# Example usage
if __name__ == "__main__":
    heap = PriorityHeap()

    # Build heap from a list of integers and floats
    data = [3, 2.1, 1, 4.5, 5, 6.3]
    heap.build_heap(data)
    print("Heap structure after building:")
    heap.print_items()

    # Add a float and an integer
    heap.add(0.8)
    print("\nHeap after adding 0.8:")
    heap.print_items()

    heap.add(7)
    print("\nHeap after adding 7:")
    heap.print_items()

    # Remove the smallest integer value
    removed_int = heap.remove_min_int()
    print(f"\nRemoved the smallest integer value: {removed_int}")
    print("\nHeap after removing the smallest integer value:")
    heap.print_items()

    # Remove the smallest float value
    removed_float = heap.remove_min_float()
    print(f"\nRemoved the smallest float value: {removed_float}")
    print("\nHeap after removing the smallest float value:")
    heap.print_items()
#output
#Heap structure after building:
#Integer values: [1, 3, 5]
#Float values: [2.1, 4.5, 6.3]

#Heap after adding 0.8:
#Integer values: [1, 3, 5]
#Float values: [0.8, 2.1, 6.3, 4.5]

#Heap after adding 7:
#Integer values: [1, 3, 5, 7]
#Float values: [0.8, 2.1, 6.3, 4.5]

#Removed the smallest integer value: 1

#Heap after removing the smallest integer value:
#Integer values: [3, 7, 5]
#Float values: [0.8, 2.1, 6.3, 4.5]

#Removed the smallest float value: 0.8

#Heap after removing the smallest float value:
#Integer values: [3, 7, 5]
#Float values: [2.1, 4.5, 6.3]
