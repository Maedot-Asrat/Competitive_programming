# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0
        
    def get(self, index: int) -> int:
        current=self.head
        if index<0 or index>=self.size:
            return -1
        while index > 0:
            current=current.next
            index-=1
        if current:
            return current.val
        else:
            return
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index: int, val: int) -> None:
        current=self.head
        new_node= ListNode(val)
        if index>self.size:
            return
        if index<=0:
            new_node.next=current
            self.head=new_node
        else:
            while index>1:
                if current:
                    current=current.next
                index-=1
            if new_node and current:
                new_node.next=current.next
                current.next=new_node
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        current = self.head
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            if current and current.next:
                current.next = current.next.next

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)