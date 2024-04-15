#import sys
#sys.path.append("C:\Users\kunal\OneDrive\CODE FOR LIFE\Python projects\Untitled Folder\DataStructures")
class Q:
    def __init__(self):
        self.items = []
    
    def enq(self, item):
        self.items.append(item)
    
    def dq(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
