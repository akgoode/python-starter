class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __repr__(self) -> str:
        node = self.head
        values = []
        while node is not None:
            values.append(str(node.value))
            node = node.next
        values.append("None")
        return " -> ".join(values)
    
    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def append(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1
        return True

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1
        return True

    def pop(self) -> int:
        node = self.head
        while node is not None:
            if(node.next.next is None):
                self.tail = node
                node_value = node.next.value
                node.next = None
                self.length -= 1
                return node_value
            node = node.next

    def pop_first(self) -> int:
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def set_value(self, index, value):
        node = self.get(index)
        if(node):
            node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if(index < 0 or index > self.length):
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        prev_node = self.get(index - 1)
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        if(index < 0 or index > self.length):
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev_node = self.get(index -1)
        removed = prev_node.next
        prev_node.next = removed.next
        self.length -= 1
        return removed
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



my_linked_list = LinkedList(4)

print(my_linked_list)

my_linked_list.append(7)

my_linked_list.prepend(12)

# print(my_linked_list.pop())
# print(my_linked_list)
# print(my_linked_list.pop_first())
# print(my_linked_list)

print(my_linked_list.get(1).value)
print(my_linked_list.get(2).value)
print(my_linked_list.get(5))

my_linked_list.set_value(2, 53)

print(my_linked_list)

my_linked_list.insert(0, 543)
print(my_linked_list)
my_linked_list.insert(3, 222)
print(my_linked_list)

my_linked_list.reverse()

print(my_linked_list)