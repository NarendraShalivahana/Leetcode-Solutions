1927.Sum_Game

class Solution:
    def sumGame(self, num: str) -> bool:
        res=0;n=len(num)
        for i in range(n//2):
            if num[i]=="?":
                res+=4.5
            else:
                res+=int(num[i])
        for i in range(n//2,n):
            if num[i]=="?":
                res-=4.5
            else:
                res-=int(num[i])
        if res!=0:
            return True
        return False


        
