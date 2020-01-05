# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        l = None
        r = None
        if root is not None:
            if val<root.val:
                l = root.left
                root.left=self.insertIntoBST(l,val)
            elif val>root.val:
                r = root.right
                root.right=self.insertIntoBST(r,val)
            return root
        if root is None:
            return TreeNode(val)
        
