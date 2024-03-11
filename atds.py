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

class UnorderedList():
    """Maintains an unordered list via a linked series of Nodes
    """

    def __init__(self):
        self.head = None
    
    def __repr__(self):
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result

    def add(self, new_data):
        """creates a new node based on the data and adds to the beginning of the list"""
        temp_node = Node(new_data)
        temp_node.set_next(self.head)
        self.head = temp_node
    
    def append(self, new_data):
        """same, but the end of the list"""
        temp_node = Node(new_data)
        temp_node.set_next(None)
        stand = self.head
        while stand.get_next() is not None:
            stand = stand.get_next()
        stand.set_next(temp_node)

    def insert(self, pos, item):
        """inserts an item at a given position and reroutes the nodes around it"""
        temp_node = Node(item)
        stand = self.head
        siit = None
        place = 0
        while place < pos:
            siit = stand
            stand = stand.get_next()
            place += 1
        if pos == 0:
            temp_node.set_next(stand)
            self.head = temp_node
        else:
            if siit.get_next() is not None:
                temp_node.set_next(stand)
                siit.set_next(temp_node)
            else:
                siit.set_next(temp_node)

    def pop_last(self):
        """logic if there is not a specified position to pop, pops the last node"""
        stand = self.head
        siit = None
        while stand.get_next() is not None:
            siit = stand
            stand = stand.get_next()
        siit.set_next(None)
        return stand.get_data()
    
    def pop(self, pos=-1):
        """removes and returns an item from the list, works even if a position is not specified"""
        if pos == -1:
            return self.pop_last()
        stand = self.head
        place = 0
        siit = None
        if pos == 0:
            siit = stand
            self.head = stand.get_next()
            return siit.get_data()
        else:
            while place < pos:
                siit = stand
                stand = stand.get_next()
                place += 1
            siit.set_next(stand.get_next())
            return stand.get_data()
    
    def length(self):
        """Traverses the entire length of the UnorderedList to identify 
        how many values (nodes) there are in the list. """
        node_count = 0                  # local variable for counting
        current = self.head             # start at the beginning
        while current != None:          # if we're not at the end of the list
            current = current.get_next()     # move to the next node
            node_count += 1                 # increment node counter
        return node_count

    def search(self, data):
        """returns a boolean based on whether an item is in the list"""
        stand = self.head
        found = False
        while stand != None and not found:
            #print(type(stnd.get_data()[0]))
            #print(type(daa))
            if stand.get_data() == data:
                found = True
            else:
                stand = stand.get_next()
        return found
    
    def index(self, item):
        """returns the location of a given item in the list"""
        node_count = 0             
        current = self.head
        if not self.search(item):
            return None
        while current.get_data() != item:     
            current = current.get_next()
            node_count += 1            
        return node_count
    
    def remove(self, data):
        """removes a specified data point from the list"""
        stand = self.head
        siiit = None
        while stand != None:
            if stand.get_data() == data:
                if siiit == None:
                    self.head = stand.get_next()
                else:
                    siiit.set_next(stand.get_next())
                if self.search(data):
                    siiit = stand
                    stand = stand.get_next()
                else:
                    return
            else:
                siiit = stand
                stand = stand.get_next()
