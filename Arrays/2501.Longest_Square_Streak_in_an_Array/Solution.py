
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        d=dict()
        n=len(nums)
        maxi=0
        for i in range(n):
            cur=nums[i]**(0.5)
            ans=d.get(cur,0)
            res=1+ans
            d[nums[i]]=res
            maxi=max(maxi,res)
        return maxi if maxi>=2 else -1
        
