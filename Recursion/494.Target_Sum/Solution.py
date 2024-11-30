494.Target_Sum
class Solution:
    def findTargetSumWays(self, nums: List[int], tar: int) -> int:
        n=len(nums)
        # dp=[None for _ in range(n+2)]
        dp=0
        @lru_cache(None)
        def f(pos,tar,n,dp):
            #print(pos,tar)
            if pos>=n:
                if tar==0 and pos>=n:
                    #print(1)
                    return 1
                return 0
            #print(pos,tar)
            
            return f(pos+1,tar+nums[pos],n,dp)+f(pos+1,tar-nums[pos],n,dp)
            
        ans=f(0,tar,n,dp)
        return ans
        
        
