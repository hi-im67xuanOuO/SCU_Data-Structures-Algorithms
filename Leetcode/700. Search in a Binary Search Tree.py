# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, target: int) -> TreeNode:
        if root is None:
            return None     
        while root is not None:
            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            elif root.val == target:
                root = root
                break
        return root
        
    
