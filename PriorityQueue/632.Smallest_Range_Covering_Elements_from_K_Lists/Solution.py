632.Smallest_Range_Covering_Elements_from_K_Lists
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        from heapq import heappush,heappop
        pq=[];n=len(nums)
        cur_max=float('-inf')
        for i in range(n):
            heappush(pq,(nums[i][0],i,0))
            cur_max=max(cur_max,nums[i][0])
        res=[float('-inf'),float('inf')]
        while pq:
            
            cur_min,l_ind,i=heappop(pq)
            # print(pq,cur_max,cur_min)
            if (res[1]-res[0]>cur_max-cur_min) or(cur_min<res[0] and (cur_max-cur_min==res[1]-res[0])):
                res[0],res[1]=cur_min,cur_max
            if i+1<len(nums[l_ind]):
                heappush(pq,(nums[l_ind][i+1],l_ind,i+1))
                cur_max=max(cur_max,nums[l_ind][i+1])
            else:
                break
        return res
