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

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self, nxt):
        self.next = nxt

    def __repr__(self):
        return "[data="+str(self.data) + ", next="+ str(self.next)+"]"
        # super().__repr__() +  -\_('-')_/- just in case

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
    def is_empty(self):
        """returns a boolean if the list is empty or not"""
        return self.length() == 0

    
class UnorderedListStack(object):
    def __init__(self):
        self.us = UnorderedList()

    def __repr__(self):
        return str(self.us)
    
    def push(self, item):
        return self.us.add(item)

    def pop(self):
        return self.us.pop(0)

    def peek(self):
        poke = self.us.pop(0)
        self.us.add(poke)
        return poke
    
    def size(self):
        return self.us.length()
    
    def is_empty(self):
        return self.us.is_empty()

class HashTable():
    def __init__(self, m):
        self.size = m
        self.slots = [None] * self.size
        self.keys =  [None] * self.size
    
    def hash_function(self, key, size):
        return key % size
    
    def put(self, key, value):
        hvalue = self.hash_function(key, self.size)
        if self.slots[hvalue] == None:
            self.slots[hvalue] = key
            self.keys[hvalue] = value
        elif self.slots[hvalue] == key:
            self.keys[hvalue] = value
        else:
            nextfree = (hvalue + 1) % self.size
            while self.slots[nextfree] != None and self.slots[nextfree] != key:
                nextfree = (nextfree+1) % self.size
            if self.slots[nextfree] == key:
                self.keys[nextfree] = value
            else:
                self.slots[nextfree] = key
                self.keys[nextfree] = value
    
    def get(self, key):
        hvalue = self.hash_function(key, self.size)
        if hvalue not in self.slots:
            return None
        elif self.slots[hvalue] != None and self.slots[hvalue] == key:
            return self.keys[hvalue]
        else:
            nextfree = (hvalue + 1) % self.size
            while self.slots[nextfree] != None and self.slots[nextfree] != key:
                nextfree = (nextfree+1) % self.size
            return self.keys[nextfree]

    def __repr__(self):
        return "Keys:   " + str(self.slots) + "\n" + "Values: " + str(self.keys)

class BinaryTree():
    def __init__(self, key):
        self.root = key
        self.left = None
        self.right = None

    def get_root_val(self):
        return self.root

    def set_root_val(self, new_val):
        self.root = new_val

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def insert_left(self, new_branch):
        newL = BinaryTree(new_branch)
        newL.left = self.left
        self.left = newL

    def insert_right(self, new_branch):
        newR = BinaryTree(new_branch)
        newR.right = self.right
        self.right = newR
    
    def __str__(self):
        return f"BinaryTree[key={self.root},\nleft_child={self.left},\nright_child={self.right}]"

class Vertex(object):
    """Describes a vertex object in terms of a "key" and a
    dictionary that indicates edges to neighboring vertices with
    a specified weight.
    """
    
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary 
        in which we'll store other vertices to which this vertex is
        connected.
        """
        self.id = key
        self.connected_to = {}   # empty dictionary for neighboring vertices
        self.color = 'white'
        self.distance = 0
        self.predecessor = None
        self.discovery_time = 0     # discovery time
        self.finish_time = 0        # finish time  
    
    def add_neighbor(self, neighbor_vertex, weight=0):
        """Adds a reference to a neighboring Vertex object to the
        dictionary, to which this vertex is connected by an edge. 
        If a weight is not indicated, default weight is 0.
        """
        self.connected_to[neighbor_vertex] = weight
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_distance(self, distance):
        self.distance = distance
    
    def get_distance(self):
        return self.distance
    
    def set_pred(self, predecessor):
        self.predecessor = predecessor
    
    def get_pred(self):
        return self.predecessor
    
    def set_discovery(self, discovery_time):
        self.discovery_time = discovery_time
    
    def get_discovery(self):
        return self.discovery_time
    
    def set_finish(self, finish_time):
        self.finish_time = finish_time
    
    def get_finish(self):
        return self.finish_time
    
    def __repr__(self):
        """Returns a representation of the vertex and its neighbors,
        suitable for printing. Check out the example of 'list
        comprehension' here!
        """
        return 'Vertex[id=' + str(self.id) \
                + ',color=' + self.color \
                + ',dist=' + str(self.distance) \
                + ',pred=' + str(self.predecessor) \
                + ',disc=' + str(self.discovery_time) \
                + ',fin=' + str(self.finish_time) \
              + '] connected_to: ' + str([x.id for x in self.connected_to]) 
    
    def get_connections(self):
        """Returns the keys of the vertices we're connected to
        """
        return self.connected_to.keys()
    
    def get_id(self):
        """Returns the id ("key") for this vertex
        """
        return self.id
    
    def get_weight(self, neighbor_vertex):
        """Returns the weight of an edge connecting this vertex 
        with another.
        """
        return self.connected_to[neighbor_vertex]

class Graph(object):
    """Describes the Graph class, which is primarily a dictionary
    mapping vertex names to Vertex objects, along with a few methods
    that can be used to manipulate them.
    """
    def __init__(self):
        """Initializes an empty dictionary of Vertex objects
        """
        self.graph = {}

    def add_vertex(self, key):
        """Creates a new "key-value" dictionary entry with the string "key"
        key as the dictionary key, and the Vertex object itself as the value.
        Returns the new vertex as a result.
        """
        new_vertex = Vertex(key)
        self.graph[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        """Looks for the key in the dictionary of Vertex objects, and
        returns the Vertex if found. Otherwise, returns None.
        """
        if key in self.graph.keys():
            return self.graph[key]
        else:
            return None

    def __contains__(self, key):
        """This 'dunder' expression is written so we can use Python's "in"
        operation: If the parameter 'key' is in the dictionary of vertices,
        the value of "key in my_graph" will be True, otherwise False.
        """
        return key in self.graph.keys()

    def add_edge(self, from_key, to_key, weight=0):
        """Adds an edge connecting two vertices (specified by key
        parameters) by modifying those vertex objects. Note that
        the weight can be specified as well, but if one isn't
        specified, the value of weight will be the default value
        of 0.
        """
        # if the from_key doesn't yet have a vertex, create it
        if from_key not in self.get_vertices():
            self.add_vertex(from_key)
        # if the to_key doesn't yet have a vertex, create it
        if to_key not in self.get_vertices():
            self.add_vertex(to_key)
        # now we can create the edge between the two
        self.get_vertex(from_key).add_neighbor(self.get_vertex(to_key), weight)

    def get_vertices(self):
        """Returns a list of the Graph's Vertex keys"""
        return self.graph.keys()

    def __iter__(self):
        """Another 'dunder' expression that allows us to iterate through
        the list of vertices.
        Example use:
        for vertex in graph:  # Python understands this now!
            print(vertex)
        """
        return iter(self.graph.values())
    
def off_by_one(v1, v2):
    count = 0
    if len(v1) != len(v2):
        return None
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            count += 1
    return count == 1
    
def make_graph():
    g = Graph()
    file = open("four_letter_words.txt")
    for line in file:
        word = line.rstrip()
        g.add_vertex(word)
    for vertex1 in g:
        for vertex2 in g:
            if off_by_one(vertex1.get_id(), vertex2.get_id()):
                g.add_edge(vertex1.get_id(), vertex2.get_id())
    return g

def breadth_first(start):
        """Does a BFS on "graph" beginning at "start" vertex, and creating a series of links between the vertices
        """
        start.set_distance(0)
        start.set_pred(None)
        queue = []
        queue.append(start)
        while len(queue) > 0:
            current_vert= queue.pop(0)
            for neighbor in current_vert.get_connections():
                #print(neighbor)
                if neighbor.get_color() == 'white':
                    neighbor.set_color('gray')
                    neighbor.set_pred(current_vert)
                    queue.append(neighbor)
            current_vert.set_color('black')

def traverse(final):
    """travels back up the graph to the start node by following the predecesors
    """
    current = final
    while current.get_pred() != None:
        print(current.get_id())
        current = current.get_pred()
    print(current.get_id())
