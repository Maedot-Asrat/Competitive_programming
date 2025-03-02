# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        odds=head
        evens=head.next
        even=evens
        while evens !=None and odds!=None and evens.next!=None and odds.next!=None:
            odds.next=evens.next
            odds=odds.next
            evens.next=odds.next
            evens=evens.next
        odds.next=even
        return head