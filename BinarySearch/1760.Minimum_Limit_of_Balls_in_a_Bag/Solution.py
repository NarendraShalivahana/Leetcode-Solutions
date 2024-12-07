1760.Minimum_Limit_of_Balls_in_a_Bag
class Solution:
    def minimumSize(self, nums: List[int], m: int) -> int:
        # if len(nums)==1:
        #     return nums[0]//m
        nums.sort()
        def f(mid,n):
            k=m
            for i in nums:
                if i<=mid:
                    continue
                else:
                    cur=0
                    if i%mid==0:
                        cur=(i//mid)-1
                    else:
                        cur=(i//mid)
                    k-=cur
                if k<0:
                    return False
            return True

        l,r=1,max(nums)*2
        res=max(nums)
        n=len(nums)
        while l<=r:
            mid=(l+r)//2
            if f(mid,n)==True:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
