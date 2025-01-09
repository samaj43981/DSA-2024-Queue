class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(f"Queue: {self.items}")

    def clear(self):
        self.items = []

    def peek_last(self):
        if not self.is_empty():
            return self.items[-1]
        return None

q = Queue()
q.clear()
q.display()  # ควรได้ Queue: []
q.enqueue(1)
q.enqueue(2)
print(q.peek_last())  # ควรได้ 2

