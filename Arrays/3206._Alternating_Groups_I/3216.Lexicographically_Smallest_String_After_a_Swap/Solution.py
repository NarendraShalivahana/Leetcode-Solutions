3216. Lexicographically Smallest String After a Swap
class Solution:
    def getSmallestString(self, s: str) -> str:
        nums=[int(i) for i in s]
        for i in range(1,len(s)):
            if nums[i]%2==nums[i-1]%2 and nums[i-1]>nums[i]:
                nums[i],nums[i-1]=nums[i-1],nums[i]
                break
        
        res=""
        for i in nums:
            res+=str(i)
        return res
