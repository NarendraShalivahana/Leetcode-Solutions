687.Longest_Univalue_Path
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.res=0
        def f(root,d):
            if root==None:
                return
            f(root.left,d)
            f(root.right,d)
            cur=1
            ls,rs=0,0
            if root.left!=None and root.val==root.left.val:
                ls=d.get(root.left,1)
            if root.right!=None and root.val==root.right.val:
                rs=d.get(root.right,1)
            self.res=max(self.res,cur+ls+rs)
            d[root]=1+max(ls,rs)
            return 
        d=dict()
        f(root,d)
        return self.res-1 if self.res>0 else 0
