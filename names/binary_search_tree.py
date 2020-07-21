class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value == value and self.right is None:
            self.right = BSTNode(value)
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
                
    def contains(self, target):
        current_node = self
        while current_node:
            if target == current_node.value:
                return True
            elif target < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
            
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()
        
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    def in_order_print(self, node):

        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)


    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)

        while len(q) > 0:
            temp = q.dequeue()
            print(temp.value)
            
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)

    def dft_print(self, node):
        stk = Stack()
        stk.push(node)

        while len(stk) > 0:
            temp = stk.pop()
            print(temp.value)

            if temp.left:
                stk.push(temp.left)
            if temp.right:
                stk.push(temp.right)

    def pre_order_dft(self, node):

        print(node.value)
        if node.left is not None:
            self.pre_order_dft(node.left)
        if node.right is not None:
            self.pre_order_dft(node.right)

    def post_order_dft(self, node):

        if node.left is not None:
            self.post_order_dft(node.left)
        if node.right is not None:
            self.post_order_dft(node.right)
        print(node.value)