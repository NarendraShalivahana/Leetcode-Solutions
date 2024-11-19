2461.Maximum_Sum_of_Distinct_Subarrays_With_Length_K
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        from collections import Counter
        c=Counter(nums[:k-1])
        n=len(nums)
        maxi=0
        total=sum(nums[:k-1])
        for i in range(k-1,n):
            c[nums[i]]+=1
            total+=nums[i]
            if len(c)==k:
                maxi=max(maxi,total)
            total-=nums[i-k+1]
            if c[nums[i-k+1]]==1:
                del c[nums[i-k+1]]
            else:
                c[nums[i-k+1]]-=1
        if len(c)==k:
            maxi=max(maxi,total)
            
        return maxi
