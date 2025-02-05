1686.Stone_Game_VI
class Solution:
    def stoneGameVI(self, a: List[int], b: List[int]) -> int:
        nums=[];n=len(a)
        for i in range(n):
            nums.append([a[i]+b[i],i])
        nums.sort(key=lambda x:(x[0]))
        nums=nums[::-1]
        alice,bob=0,0
        for i in range(0,n):
            if i%2==0:
                alice+=a[nums[i][1]]
            else:
                bob+=b[nums[i][1]]
        if alice==bob:
            return 0
        elif alice>bob:
            return 1
        return -1
        
