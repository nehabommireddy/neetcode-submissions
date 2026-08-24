# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(pnode, qnode):
            if pnode is None and qnode is None:
                return True
            if not pnode and qnode:
                return False
            if not qnode and pnode:
                return False
            if pnode.val != qnode.val:
                return False
            return isSame(pnode.left, qnode.left) and isSame(pnode.right, qnode.right)
        
        return isSame(p, q)
