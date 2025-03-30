# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = []

        def traversal(node:TreeNode):
            tl = node.left
            tr = node.right
            if tl:
                traversal(tl)
            
            node.left = None
            node.right = None
            q.append(node)

            if tr:
                traversal(tr)
        
        traversal(root)
        n = len(q)
        
        def recur(node, l_ls, r_ls):
            
            if l_ls:
                m = len(l_ls)
                if m ==1 :
                    node.left = l_ls[0]
                else:
                    i = (m-1)//2
                    ln = l_ls[i] 
                    node.left = ln
                    recur(ln, l_ls[:i], l_ls[i+1:])

            if r_ls:
                m = len(r_ls)
                if m == 1:
                    node.right = r_ls[0]
                else:
                    i = (m-1)//2
                    rn = r_ls[i]
                    node.right = rn
                    recur(rn, r_ls[:i], r_ls[i+1:])

        m = (n-1)//2
        new_root = q[m]

        recur(new_root, q[:m], q[m+1:])
        return new_root