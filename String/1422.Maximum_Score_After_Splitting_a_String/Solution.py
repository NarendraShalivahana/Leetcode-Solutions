1422.Maximum_Score_After_Splitting_a_String
class Solution:
    def maxScore(self, s: str) -> int:
        res=0
        z,o=0,s.count('1')
        for i in s[:-1]:
            if i=="0":
                z+=1
            else:
                o-=1
            res=max(res,z+o)
        return res
