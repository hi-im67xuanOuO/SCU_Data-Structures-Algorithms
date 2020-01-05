# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        res = []
        self.inOrder(root, res)
        return res == sorted(res) and len(res) == len(set(res))
        
    def inOrder(self, root, res):
        if not root: return []
        l = self.inOrder(root.left, res)
        if l:
            res.extend(l)
        res.append(root.val)
        r = self.inOrder(root.right, res)
        if r:
            res.extend()
