class Node:
    """
    An object for storing a single node of linked a list.
    Models two attribute - data and the linked to the node in the list

    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node Data: %s>" % self.data
    

class Linked_list:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    

    def size(self):
        """
        Returns the numbers of the list 
        takes O(n) times
        """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    def add (self, data):
        """
        Adds a new node containing data at head of the list
        takes O(1) times
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    def __repr__(self):
        """
        Return a string representation of the list
        takes O(n) times
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data) 
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)

