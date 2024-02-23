class Stack(object):
    """
    Describes a stack that can be pushed and popped
    """
    def __init__(self):
        # creates the stack (bottom = stack[0], top = stack[-1])
        self.stk = []

    #def prlis(self):
    #    print(self.stk[0:])
    
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
    
    #def prlis(self):
    #    print(self.q[0:])
    
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
