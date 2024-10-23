# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        
        dq=deque()
        dq.append([root,root]);d=dict()
        while len(dq)>0:
            temp=[]
            if len(dq)>1:
                # print(dq)
                tot=0
                d1=dict()
                d2=dict()
                for u,v in dq:
                    cur=d1.get(v,[])
                    cur.append(u)
                    d1[v]=cur
                    d2[v]=d2.get(v,0)+u.val
                    tot+=u.val
                for i in d1:
                    for j in d1[i]:
                        d[j]=tot-d2[i]
                    
            while len(dq)>0:
                cur=dq.popleft()
                if cur[0].left!=None:
                    temp.append([cur[0].left,cur[0]])
                if cur[0].right!=None:
                    temp.append([cur[0].right,cur[0]])
                
                    
            dq+=temp
        def f(root):
            if root==None:
                return 
            root.val=0
            f(root.left)
            f(root.right)
        f(root)
        for i in d:
            i.val=d[i]
        root.val=0
        return root
                
                
        
