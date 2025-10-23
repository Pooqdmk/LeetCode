class Node:
    def __init__(self,val = 0,next = None):
        self.next = next
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.l = Node()

    def get(self, index: int) -> int:
        cur = self.l.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i+=1
            cur = cur.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val = val,next = self.l.next)
        self.l.next = newNode


    def addAtTail(self, val: int) -> None:
        newNode = Node(val = val)
        cur = self.l
        while cur and cur.next:
            cur = cur.next
        cur.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.l
        i=0
        while i<index and cur.next:
            i+=1
            cur = cur.next
        if i!=index:
            return 
        newNode = Node(val=val, next=cur.next)
        cur.next = newNode



    def deleteAtIndex(self, index: int) -> None:
        i = 0
        
        cur = self.l.next
        prev = self.l
        while cur:
            if i == index:
                prev.next = cur.next
                break
            i+=1
            prev = cur
            cur = cur.next

        
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)