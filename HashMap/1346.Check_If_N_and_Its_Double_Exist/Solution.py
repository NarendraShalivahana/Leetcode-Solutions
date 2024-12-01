class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d=dict()
        for i in arr:
            d[i]=d.get(i,0)+1
        if d.get(0,-1)>=2:
            return True
        for i in arr:
            if i!=0 and d.get(2*i,0)==1:
                return True
        return False
        
