2779.Maximum_Beauty_of_an_Array_After_Applying_Operation
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        from heapq import heappush,heappop
        nums.sort();arr=[];n=len(nums)
        for i in range(n):
            arr.append([nums[i]-k,nums[i]+k])
        res=0;pq=[];i=0
        while i<n:
            while pq and pq[0]<arr[i][0]:
                heappop(pq)
            heappush(pq,arr[i][1])
            res=max(res,len(pq))
            i+=1
        return res
            
        
        
            
        
