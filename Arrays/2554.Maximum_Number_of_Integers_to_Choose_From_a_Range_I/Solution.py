2554.Maximum_Number_of_Integers_to_Choose_From_a_Range_I
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res=[i for i in range (n+1)]
        for i in banned:
            if i<n+1:
                res[i]=False
        
        cur=0
        cnt=0
        # print(res)
        for i in res[1:]:
            if i==False:
                continue
            elif cur+i>maxSum:
                break
            else:
                # print(i)
                cnt+=1
                cur+=i
        return cnt
            
        
