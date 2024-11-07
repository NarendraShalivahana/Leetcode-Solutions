class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res=0
        i=1
        while i<10**8:
            cur=0
            for j in candidates:
                if j&i>0:
                    cur+=1
            res=max(res,cur)
            i<<=1
        return res
