274.H-Index
class Solution:
    def hIndex(self, nums: List[int]) -> int:
        arr=[0 for _ in range(1001)]
        for i in nums:
            arr[i]+=1
        
        for i in range(999,-1,-1):
            arr[i]+=arr[i+1]
        
        for i in range(1000,-1,-1):
            if arr[i]>=i:
                return i
        return 0
