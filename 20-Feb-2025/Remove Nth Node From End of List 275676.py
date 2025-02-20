# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=ListNode(None)
        current.next=head
        aheadptr=current.next
        while n>0:
            aheadptr=aheadptr.next
            n-=1
        behindptr=current.next
        prev=None
        while aheadptr:
            prev=behindptr
            behindptr=behindptr.next
            aheadptr=aheadptr.next
        if not prev:
            head=behindptr.next
        else:
            prev.next=behindptr.next
        return head
        
        

