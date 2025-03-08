# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listt=[]
        curr=head
        while curr:
            listt.append(curr.val)
            curr=curr.next
        for i in range(0,len(listt)-k+1,k):
            listt[i:i+k]=reversed(listt[i:i+k])
        dummy=ListNode()
        curr=dummy
        for val in listt:
            curr.next=ListNode(val)
            curr=curr.next
        return dummy.next