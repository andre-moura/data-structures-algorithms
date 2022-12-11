class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.tail = self.new_node
        self.length = 1


    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node
        self.length += 1
        return True


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
        

            
    def pop(self):
        if self.length == 0:
            return

        pre = temp = self.head
        while temp.next != None:
            pre = temp
            temp = temp.next

        self.tail = pre
        pre.next = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return temp
        
    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value


    


    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next