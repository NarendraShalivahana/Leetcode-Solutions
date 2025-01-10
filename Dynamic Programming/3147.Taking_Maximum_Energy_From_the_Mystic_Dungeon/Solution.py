3147.Taking_Maximum_Energy_From_the_Mystic_Dungeon

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        maxi=float('-inf');n=len(energy)
        dp=[0 for i in range(n)]
        for i in range(n):
            if i-k>-1:
                dp[i]=max(energy[i]+dp[i-k],energy[i])
            else:
                dp[i]=energy[i]
            if i+k>=n:
                
                maxi=max(maxi,dp[i],energy[i])
            # print(dp)
            
            
        # temp=max(energy[n-k:n])
        
        return maxi
        
