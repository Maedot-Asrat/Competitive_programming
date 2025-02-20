# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        prev=None
        while current :
            if prev:
                if current.val==prev.val:
                    prev.next=current.next
                    current=current.next
                    continue
                prev =current
                current=current.next
            else:
                prev=current
                current=current.next   
        return head