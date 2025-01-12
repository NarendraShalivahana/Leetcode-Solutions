2415.Reverse_Odd_Levels_of_Binary_Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        dq=deque([root])
        res=[]
        while len(dq)>0:
            nodes,vals=[],[]
            while len(dq)>0:
                cur=dq.popleft()
                vals.append(cur.val)
                if cur.left!=None:
                    nodes.append(cur.left)
                if cur.right!=None:
                    nodes.append(cur.right)
            dq+=nodes
            res.append(vals)
        oth=[]
        for i in range(len(res)):
            if i%2!=0:
                res[i]=res[i][::-1]
            oth+=res[i]
                
        dq=deque([root])
        dq2=deque(oth.copy())
        #print(dq2)
        res=[]
        while len(dq)>0:
            nodes=[]
            while len(dq)>0:
                cur=dq.popleft()
                curval=dq2.popleft()
                cur.val=curval
                if cur.left!=None:
                    nodes.append(cur.left)
                if cur.right!=None:
                    nodes.append(cur.right)
            dq+=nodes
        return root
        
                    
                
        
