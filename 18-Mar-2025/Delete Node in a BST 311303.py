# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node):
            while node.left:
                node=node.left
            return node
        def search(node):
            if not node:
                return None
            if node.val==key:
                if not node.left and not node.right:
                    return None
                elif node.left and not node.right:
                    return node.left
                elif node.right and not node.left:
                    return node.right
                else:
                    successor =find_min(node.right)
                    node.val=successor.val
                    successor.val=key
                    node.right = search(node.right)
                    return node
            elif node.val > key:
                node.left = search(node.left)
                return node
            elif node.val < key:
                node.right = search(node.right)
                return node
        root=search(root)
        return root