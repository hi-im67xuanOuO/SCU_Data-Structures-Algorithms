# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.inorder_recursive(root,res)
        return res
     
    def inorder_recursive(self,root,res):
        if root:
            self.inorder_recursive(root.left,res)
            res.append(root.val)
            self.inorder_recursive(root.right,res)
