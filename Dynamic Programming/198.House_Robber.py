#198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        first=nums[0]
        second=max(nums[:2])
        if len(nums)<=2:
            return second
        for i in range(2,len(nums)):
            cur=max(nums[i]+first,second)
            first=second
            second=cur
        return second
