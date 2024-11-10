124.Binary_Tree_Maximum_Path_Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=float('-inf')
        def f(root):
            if root==None:
                return 0
            lr=f(root.left)
            rr=f(root.right)
            self.res=max(self.res,root.val,root.val+lr+rr,root.val+max(lr,rr))
            return max(root.val,root.val+max(lr,rr))
        re=f(root)
        return self.res
