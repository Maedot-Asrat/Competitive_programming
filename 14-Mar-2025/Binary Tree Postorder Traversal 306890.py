# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        head = root
        self.ans = []
        self.recur(head)
        return self.ans
    def recur(self,head):
        if not head:
            return
        self.recur(head.left)
        self.recur(head.right)        
        self.ans.append(head.val)
