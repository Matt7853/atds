class Stack(object):
    """
    Describes a stack that can be pushed and popped
    """
    def __init__(self):
        # creates the stack (bottom = stack[0], top = stack[-1])
        self.stk = []
    
    def __repr__(self):
        return str(self.stk)
    
    def push(self, item):
        # adds an item to the top of the stack
        return self.stk.append(item)
        
    def pop(self):
        # removes an item only from the top of the stack, returns it
        if len(self.stk) > 0:
            return self.stk.pop(-1)
        else:
            return None

    def peek(self):
        # returns only the top item, doesn't remove it
        if len(self.stk) > 0:
            return self.stk[-1]
        else:
            return None
    
    def is_empty(self):
        # checks if the stack is empty (True = empty)
        return len(self.stk) == 0

    def size(self):
        # returns the number of items in the stack
        return len(self.stk)
    
class Queue(object):
    def __init__(self):
        self.q = []
        
    def __repr__(self):
        return str(self.q)

    def enqueue(self, item):
        return self.q.append(item)
    
    def dequeue(self):
        if len(self.q) > 0:
            return self.q.pop(0)
        else:
            return None
        
    def peek(self):
        if len(self.q) > 0:
            return self.q[0]
        else:
            return None
    
    def size(self):
        return len(self.q)
    
    def is_empty(self):
        return len(self.q) == 0

class Deque(object):
    def __init__(self):
        self.d = []
    
    def __repr__(self):
        return str(self.d)

    def add_front(self, item):
        return self.d.insert(0, item)

    def add_rear(self, item):
        return self.d.append(item)
    
    def remove_front(self):
        if len(self.d) > 0:
            return self.d.pop(0)
        else:
            return None
        
    def remove_rear(self):
        if len(self.d) > 0:
            return self.d.pop(-1)
        else:
            return None
    
    def size(self):
        return len(self.d)
    
    def is_empty(self):
        return len(self.d) == 0
