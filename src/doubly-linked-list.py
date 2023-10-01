class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def __repr__(self) -> str:
        node = self.head
        values = []
        while node is not None:
            values.append(str(node.value))
            node = node.next
        list_string = " <-> ".join(values)
        list_string += " -> None"
        return list_string
    
    def append(self, value):
        node = Node(value)
        node.prev = self.tail
        self.tail.next = node
        node.next = None
        self.tail = node
        self.length += 1
        return True

    def prepend(self, value):
        node = Node(value)
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1
        return True

    def pop(self):
        if self.length > 1:
            node = self.tail
            self.tail = node.prev
            node.prev = None
            self.tail.next = None
            self.length -= 1
            return node
        
    def pop_first(self):
        if self.length > 1:
            node = self.head
            self.head = node.next
            self.head.prev = None
            node.next = None
            self.length -= 1
            return node
        
    def get(self, index):
        if(index < 0 or index >= self.length):
            return None
        if(index == self.length - 1):
            return self.tail
        if(index == 0):
            return self.head
        
        node = self.head
        for _ in range(index):
            node = node.next

        return node
    
    def insert(self, index, value):
        if(index < 0 or index > self.length):
            return False
        if(index == self.length):
            return self.append(value)
        if(index == 0):
            return self.prepend(value)

        prev = self.get(index - 1)
        node = prev.next
        new_node = Node(value)
        new_node.prev = node.prev
        new_node.next = node
        node.prev = new_node
        prev.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if(index < 0 or index > self.length):
            return None
        if(index == self.length - 1):
            return self.pop()
        if(index == 0):
            return self.pop_first()
        
        prev = self.get(index - 1)
        node = prev.next
        next = node.next
        prev.next = next
        next.prev = prev
        self.length -= 1
        return node




dll = DoublyLinkedList(7)
dll.append(12)
dll.append(25)
dll.prepend(16)
print(dll)
node = dll.get(2)
node2 = dll.get(3)

dll.insert(1, 32)
dll.insert(4, 91)
dll.insert(3, 52)

dll.remove(4)

print(dll)