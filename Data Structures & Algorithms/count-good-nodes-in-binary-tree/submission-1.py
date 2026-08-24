# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs (root, m):
            if not root:
                return 0

            if root.val >= m:
                good = 1
            else:
                good = 0

            m = max(m, root.val)

            return good + dfs(root.left, m) + dfs(root.right, m)
        return dfs(root, root.val)



        