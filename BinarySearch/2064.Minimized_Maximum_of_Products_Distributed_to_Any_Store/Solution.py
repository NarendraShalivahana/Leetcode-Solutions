2064.Minimized_Maximum_of_Products_Distributed_to_Any_Store
class Solution:
    def minimizedMaximum(self, n: int, arr: List[int]) -> int:
        if n==len(arr):
            return max(arr)
        def f(mid):
            cnt=0
            for i in arr:
                if i>=mid:
                    if i%mid==0:
                        cnt+=(i//mid)
                    else:
                        cnt+=(i//mid)
                        cnt+=1
                else:
                    cnt+=1
            if cnt<=n:
                return True
            return False

        l,r=1,10**10
        res=-1
        while l<=r:
            mid=(l+r)//2
            if f(mid)==True:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
