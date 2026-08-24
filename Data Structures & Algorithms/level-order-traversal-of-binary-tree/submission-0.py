# Definition for a binary tree node.
from collections import deque
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        visited = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for i in range (len(queue)):
                current = queue.popleft()
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            visited.append(level)

        return visited