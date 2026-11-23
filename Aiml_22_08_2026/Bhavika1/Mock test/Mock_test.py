#implement Queue Using a stack
#class of stack and class of queue
import sys
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

class Queue:
    def __init__(self):
        self.stack1 = Stack()   #for inserting elements
        self.stack2 = Stack()   #to store elements for dequeuing

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.stack2.pop()

    def peek(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise IndexError("peek from empty queue")
        return self.stack2.peek()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()


q=Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # Output: 10
print(q.dequeue())  # Output: 20

q.enqueue(40)

print("front element:", q.peek())  # Output: 30
print(q.dequeue())  # Output: 30
print(q.dequeue())  # Output: 40

