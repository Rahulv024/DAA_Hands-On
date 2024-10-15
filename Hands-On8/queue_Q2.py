class Queue:
    def __init__(self, size):
        self.queue = [0] * size  # Fixed-size array
        self.front = 0
        self.rear = -1
        self.size = size
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue Overflow")
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def front_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            idx = self.front
            items = []
            for _ in range(self.count):
                items.append(self.queue[idx])
                idx = (idx + 1) % self.size
            print("Array:", items)

# Example usage:
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.display()  # Output queue contents
print("Front element:", queue.front_element())
print("Dequeue element:", queue.dequeue())
queue.display()
print("Dequeue element:", queue.dequeue())
queue.display()
