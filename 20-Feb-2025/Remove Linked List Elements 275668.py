# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current=ListNode(None)
        current.next=head
        prev=current
        while prev and prev.next:
            if prev.next.val==val:
                prev.next=prev.next.next
            else:
                prev=prev.next
        return current.next
        