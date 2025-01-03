2270.Number_of_Ways_to_Split_Array
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre,c1=[],0;n=len(nums)
        # pos,c2=[],0
        for i in nums:
            c1+=i
            pre.append(c1)
        # arr=nums[::-1]
        # #print(pre)
        # for i in arr:
        #     c2+=i
        #     pos.append(c2)
        # pos=pos[::-1]
        res=0
        # n=len(nums)
        for i in range(n-1):
            if pre[i]>=pre[n-1]-pre[i]:
                res+=1
        return res
        
        
            
