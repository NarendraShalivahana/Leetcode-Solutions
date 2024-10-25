class Solution:
    def maximumPoints(self, nums: List[int], ce: int) -> int:
        nums.sort()
        if nums[0]<=ce:
            return (ce+sum(nums[1:]))//nums[0]
        return 0
