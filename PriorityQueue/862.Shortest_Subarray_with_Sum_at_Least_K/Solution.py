862.Shortest_Subarray_with_Sum_at_Least_K
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        from collections import deque
        n=len(nums);l=0
        res=float('inf');cur=0
        dq=deque()
        dq.append([-1,0])
        for i in range(n):
            cur+=nums[i]
            if nums[i]>=0:
                while len(dq)>0 and cur-dq[0][1]>=k:
                    res=min(res,i-dq.popleft()[0])
            else:
                while len(dq)>0 and cur<=dq[-1][1]:
                    dq.pop()
            dq.append([i,cur])
            # print(dq)
        return res if res<=n else -1
