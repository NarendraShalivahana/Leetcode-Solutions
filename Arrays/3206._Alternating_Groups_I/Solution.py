3206. Alternating Groups I
class Solution:
    def numberOfAlternatingGroups(self, nums: List[int]) -> int:
        res=0;n=len(nums)
        for i in range(n):
            f,l=nums[(i-1)%n],nums[(i+1)%n]
            if f==l and f!=nums[i]:
                res+=1
        return res
        
