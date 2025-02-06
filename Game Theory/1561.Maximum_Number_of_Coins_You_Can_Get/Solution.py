1561.Maximum_Number_of_Coins_You_Can_Get
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)
        res=0
        j,k,l=0,n-2,n-1
        for i in range(n//3):
            res+=piles[k]
            k-=2
        return res
