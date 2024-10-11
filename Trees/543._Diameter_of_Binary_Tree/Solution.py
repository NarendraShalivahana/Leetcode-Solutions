# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def f(root):
            if root==None:
                return 0
            lh=f(root.left)
            rh=f(root.right)
            self.res=max(self.res,1+lh+rh)
            return 1+max(lh,rh)
        f(root)
        return self.res-1
