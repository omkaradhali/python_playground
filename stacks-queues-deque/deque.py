class Deque(Object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRead(self):
        return self.items.pop(0)