'''
    PROBLEM: Create a program to implement Linked List and it's CRUD Operations.

    STEPS:
        1. Linked List nodes
        2. Print the linked list
        3. Insert new nodes
        4. Delete node from Linked List
        5. Create Doubly Linked List
'''
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, value):
        self.node = Node(value)
        current = self.head

        if(current):
            while(current.next):
                current = current.next
            current.next = self.node
        else:
            self.head = self.node

    def delete(self, value):
        # Assuming that Linked List has atleast 1 node
        if(self.head.data == value):
            self.head = self.head.next
        else:
            prev = self.head
            current = prev.next

            while(current):
                if(current.data == value):
                    current = current.next
                    prev.next = current
                else:
                    prev = current
                    current = current.next
#             P --------> C
# H --> a --> b --> c --> d --> X

    def printList(self):
        current = self.head
        print("H -->", end=" ")

        while(current):
            print(current.data + " -->", end=" ")
            current = current.next
        print("X")

if __name__ == "__main__":
    list_obj = LinkedList()
    list_obj.insert('a')
    list_obj.insert('b')
    list_obj.insert('c')
    list_obj.insert('d')
    list_obj.delete('a')
    list_obj.printList()