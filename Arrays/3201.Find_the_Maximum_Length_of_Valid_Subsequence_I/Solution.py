3201.Find_the_Maximum_Length_of_Valid_Subsequence_I
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd,even=0,0
        for i in nums:
            if i%2:
                odd+=1
            else:
                even+=1
        res=max(odd,even)
        arr=[]
        for i in nums:
            if arr==[]:
                arr.append(i)
            elif arr[-1]%2==0 and i%2:
                arr.append(i)
            elif arr[-1]%2 and i%2==0:
                arr.append(i)
        return max(res,len(arr))
