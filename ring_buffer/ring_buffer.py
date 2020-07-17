class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.position = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            if self.position < self.capacity and self.position != 5:
                self.storage.pop(self.position)
                self.storage.insert(self.position, item)
                self.position += 1
            elif self.position == self.capacity:
                self.position = 0
                self.storage.remove(self.storage[self.position])
                self.storage.insert(self.position, item)
                self.position += 1
            elif self.position == 0:
                self.storage.remove(self.storage[self.position])
                self.storage.insert(self.position, item)
                self.position += 1
            else:
                self.storage.remove(self.storage[self.position])
                self.storage.insert(self.position, item)
                self.position = 0
        else:
            self.storage.append(item)

    def get(self):
        return self.storage

# mybuffer = RingBuffer(5)
# mybuffer.append("A")
# mybuffer.append("B")
# mybuffer.append("C")
# mybuffer.append("D") 
# mybuffer.append("E")
# mybuffer.append("F")
# mybuffer.append("G")
# mybuffer.append("H")
# mybuffer.append("I")
# mybuffer.append("J")
# mybuffer.append("K")
# mybuffer.append("A")
# mybuffer.append("B")
# mybuffer.append("C")



# from collections import deque

# class RingBufferDeque:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = deque(maxlen=capacity)
#         self.position = 0

#     def append(self, item):
#         self.storage.append(item)

#     def get(self):
#         return self.storage