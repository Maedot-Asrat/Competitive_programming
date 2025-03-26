# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, path):
            if(not node): return
            path = path * 10 + node.val 
            if(not node.left and not node.right):
                self.res += path
            else:
                dfs(node.left, path)
                dfs(node.right, path)
        dfs(root, 0)
        return self.res