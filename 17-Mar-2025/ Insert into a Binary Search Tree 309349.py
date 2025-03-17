# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node=TreeNode(val)
        current=root
        if not current:
            current=new_node
            return current
        while current:
            if not current.right and new_node.val>current.val:
                current.right=new_node
            if not current.left and new_node.val<current.val:
                current.left=new_node
            if current.val>val:
                current=current.left
            else:
                current=current.right
        return root
