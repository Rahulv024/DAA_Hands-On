class Stack:
    def __init__(self, size):
        self.stack = [0] * size  # Fixed-size array
        self.top = -1  # Start with an empty stack
        self.size = size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack Overflow")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top]

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Array:", self.stack[:self.top + 1])

# Example usage:
stack = Stack(5)
stack.push(2)
stack.push(10)
stack.push(24)
stack.push(49)
stack.display()  # Output stack contents
print("Top element:", stack.peek())
print("Pop element:", stack.pop())
stack.display()
stack.pop()


#OUTPUT:
#Array: [2, 10, 24, 49]
#Top element: 49
#Pop element: 49
#Array: [2, 10, 24]
