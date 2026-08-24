# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameSubtree(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return sameSubtree(root.left, subRoot.left) and sameSubtree(root.right, subRoot.right)
            else:
                return False
        
        def dfs(node):
            if not node:
                return False
            if sameSubtree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        
        return dfs(root)
