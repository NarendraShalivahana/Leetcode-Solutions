238.Product_of_Array_Except_Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=nums.count(0)
        res=[0 for _ in range(n)]
        if a>1:
            return res
        product=1
        ind=-1
        for i in range(n):
            if nums[i]==0:
                ind=i
                continue
            product*=nums[i]
        if a==1:
            res[ind]=product
            return res
        for i in range(n):
            res[i]=product//nums[i]
        return res
            
            
        
