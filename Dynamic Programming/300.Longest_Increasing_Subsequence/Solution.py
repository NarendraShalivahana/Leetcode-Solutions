//300. Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def f(cur,arr):
            l=0;r=len(arr)-1
            mid=(l+r)//2
            ans=0
            while l<=r:
                mid=(l+r)//2
                if arr[mid]>=cur:
                    ans=mid
                    r=mid-1
                else:
                    l=mid+1
            return ans
        n=len(nums)
        arr=[]
        for i in range(n):
            if arr==[]:
                arr.append(nums[i])
            elif arr[-1]<nums[i]:
                arr.append(nums[i])
            elif arr[-1]>nums[i]:
                ind=f(nums[i],arr)
                arr[ind]=nums[i]
        return len(arr)
        
