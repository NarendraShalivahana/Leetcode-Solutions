769.Max_Chunks_To_Make_Sorted
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[0 for _ in range(n)]
        # 2 0 1
        # 1 1 1
        # 1 0 2 3 4
        # 1 
        # 1 4 3 6 0 7 8 2 5 
        # 1 1 1 1 1 1 1 1 1
        cnt=1
        for i in range(n):
            if arr[i]==i and dp[i]==0:
                dp[i]=cnt
                cnt+=1
            else:
                for j in range(i,arr[i]+1):
                    if dp[i]!=0:
                        dp[j]=dp[i]
                    else:
                        dp[j]=cnt
                        cnt+=1
                    
        #print(dp)
        return max(dp)
                    
