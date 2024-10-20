class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n=len(nums)
        cur=nums[0];ind=0;res=0
        for i in range(1,n):
            if cur<nums[i]:
                res+=(i-ind)*cur
                cur=nums[i];ind=i
            elif i==n-1:
                res+=(i-ind)*cur
        return res
