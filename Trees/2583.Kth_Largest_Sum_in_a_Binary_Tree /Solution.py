# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        from collections import deque
        from heapq import heappush,heappop
        dq=deque([root])
        pq=[]
        while len(dq)>0:
            res=[];cur=0
            while len(dq)>0:
                node=dq.popleft()
                cur+=node.val
                if node.left!=None:
                    res.append(node.left)
                if node.right!=None:
                    res.append(node.right)
            dq+=res
            heappush(pq,-1*cur)
        if len(pq)<k:
            return -1
        ans=-1
        while k>0 and len(pq)>0:
            ans=-1*heappop(pq)
            k-=1
        return ans 
            
            
            
            
        
