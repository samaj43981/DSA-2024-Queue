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

class SalonQueue:
    def __init__(self):
        self.queue = Queue()
        self.services = []
        self.times = {"ตัดผม": 30, "สระ": 20, "ย้อมสี": 60}
        
    def add_customer(self, name, service):
        self.queue.enqueue(name)
        self.services.append(service)
        print(f"เพิ่มลูกค้า {name} ({service}) เข้าคิว")
    
    def show_queue(self):
        print("คิวลูกค้า:")
        total_time = 0
        for i, name in enumerate(self.queue.items):
            service = self.services[i]
            time = self.times[service]
            total_time += time
            print(f"{i+1}. {name} - {service} (รอประมาณ {total_time} นาที)")
    
    def serve_customer(self):
        if not self.queue.is_empty():
            customer = self.queue.dequeue()
            service = self.services.pop(0)
            print(f"กำลังให้บริการ {customer} ({service})")
        else:
            print("ไม่มีลูกค้าในคิว")

salon = SalonQueue()
salon.add_customer("สมชาย", "ตัดผม")
salon.add_customer("สมหญิง", "ย้อมสี")
salon.show_queue()
salon.serve_customer()
salon.show_queue()
