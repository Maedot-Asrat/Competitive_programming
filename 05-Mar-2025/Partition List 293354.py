# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lower_head = ListNode(0)
        higher_head = ListNode(0)  
        lower = lower_head
        higher = higher_head
        while head:
            if head.val < x:
                lower.next = head
                lower = lower.next
            else:
                higher.next = head
                higher = higher.next
            head = head.next

        # Connect the two lists
        lower.next = higher_head.next
        higher.next = None

        return lower_head.next
