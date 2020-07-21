class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)
        self.head = node

    def add_to_tail(self, value):
        node = Node(value)

        if self.tail is not None:
            self.tail.next = node
        self.tail = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # def reverse_list(self, node, prev): what the _ is prev????
    def reverse_list(self, node, prev):
        marker1 = None
        marker2 = self.head
        
        while marker2 is not None:
            marker3 = marker2.next
            marker2.next = marker1
            marker1 = marker2
            marker2 = marker3
        self.head = marker1

    def reverse_recursive_list(self, node, prev):
        if self.head is None:
            return
        cascade = False
        next = None
        
        if node.next is None: 
            self.head = node
            cascade = True
        next = node.next
        node.next = prev

        if cascade == True:
            return
        self.reverse_recursive_list(next, node)
        

myLL = LinkedList()
myLL.add_to_head(1)
myLL.add_to_head(2)
myLL.add_to_head(3)
myLL.add_to_head(4)
myLL.add_to_head(5)
myLL.reverse_recursive_list(myLL.head, None)
