# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for i, value in enumerate(inorder):
            dic[value] = i
        
        preIndex = 0
        def build(left, right):
            nonlocal preIndex
            if left > right:
                return None
            
            node = TreeNode(preorder[preIndex])
            preIndex+= 1
            mid = dic[node.val]
            node.left = build(left, mid-1)
            node.right = build(mid+1, right)
            return node
        
        return build(0, len(preorder)-1)