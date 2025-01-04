965.Univalued_Binary_Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def checkunival(root,value):
            if root==None:
                return True
            if root.val!=value:
                return False
            return checkunival(root.left,value) and checkunival(root.right,value)
        value=root.val
        res=checkunival(root,value)
        return res
            
