# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        head = root
        self.ans = []
        self.recur(head)
        return self.ans
    def recur(self,head):
        if not head:
            return
        self.recur(head.left)
        self.ans.append(head.val)
        self.recur(head.right)        

