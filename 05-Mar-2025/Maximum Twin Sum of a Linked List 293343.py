# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        second_half = head
        fast = head
        reversed_first = None
        while fast and fast.next:
            fast = fast.next.next
            prev = second_half.next
            second_half.next = reversed_first
            reversed_first = second_half
            second_half = prev
        s = 0
        while reversed_first and second_half:
            s = max(s,reversed_first.val + second_half.val)
            reversed_first = reversed_first.next
            second_half = second_half.next
        return s