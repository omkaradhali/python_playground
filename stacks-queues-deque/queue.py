class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items) 
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeu(self):
        self.items.pop()