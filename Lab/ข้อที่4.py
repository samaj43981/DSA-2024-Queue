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

class BankQueue:
    def __init__(self):
        self.queue = Queue()
        self.transactions = []
        
    def add_customer(self, name, transaction_type):
        self.queue.enqueue(name)
        self.transactions.append(transaction_type)
        print(f"เพิ่มลูกค้า {name} ({transaction_type}) เข้าคิว")
    
    def serve_customer(self):
        if not self.queue.is_empty():
            customer = self.queue.dequeue()
            transaction = self.transactions.pop(0)
            print(f"กำลังให้บริการ {customer} ({transaction})")
        else:
            print("ไม่มีลูกค้าในคิว")
    
    def show_queue(self):
        print("คิวลูกค้า:")
        for i, name in enumerate(self.queue.items):
            print(f"{i+1}. {name} - {self.transactions[i]}")
        print(f"จำนวนคิวทั้งหมด: {self.queue.size()}")
        print(f"ประมาณเวลารอ: {self.queue.size() * 5} นาที")
        
bank = BankQueue()
bank.add_customer("สมชาย", "ฝากเงิน")
bank.add_customer("สมหญิง", "ถอนเงิน")
bank.show_queue()
bank.serve_customer()
bank.show_queue()
