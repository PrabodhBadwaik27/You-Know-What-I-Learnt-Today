'''
    PROBLEM: Create a program to implement Double-Ended Linked List and it's CRUD Operations.

    STEPS:
        1. Linked List nodes
        2. Print the linked list
        3. Insert new nodes
        4. Delete node from Linked List
'''


class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        self.node = Node(value)
        current = self.node

        if(self.head):
            self.tail.next = current
            current.prev = self.tail
            self.tail = current
        else:
            self.head = current
            self.tail = current

        self.tail.next = self.head
        self.head.prev = self.tail

    def delete(self, value):
        # Assuming that Linked List has atleast 1 node
        if (self.head.data == value):
            if (self.head == self.tail):
                self.head = None
                self.tail = None
            else:
                current = self.head
                current.prev.next = current.next
                current.next.prev = current.prev
                self.head = current.next
        elif (self.tail.data == value):
            self.tail = self.tail.prev
            self.tail.next = self.head
        else:
            current = self.head.next
            while(current.data != value and current != self.head):
                current = current.next
            if (current.data == value):
                current.prev.next = current.next
                current.next.prev = current.prev
        '''
        if (self.head.data == value):
            if (self.head == self.tail):
                self.head = None
                self.tail = None
            else:
                current = self.head
                current.prev.next = current.next
                current.next.prev = current.prev
        elif(self.tail.data == value):
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev = self.head
            current = prev.next

            while (current):
                if (current.data == value):
                    current = current.next
                    prev.next = current
                    current.prev = prev
                else:
                    prev = current
                    current = current.next
        '''
    #             P --------> C
    # H --> a --> b --> c --> d --> X

    def printList(self):
        current = self.head
        print("H -->", end=" ")

        while (current and current != self.tail):
            print(current.data + " <-->", end=" ")
            current = current.next
        print(current.data + " <--> ", end=" ")
        print("H")


if __name__ == "__main__":
    list_obj = LinkedList()
    list_obj.insert('a')
    list_obj.insert('b')
    list_obj.insert('c')
    list_obj.insert('d')
    list_obj.delete('d')
    list_obj.printList()