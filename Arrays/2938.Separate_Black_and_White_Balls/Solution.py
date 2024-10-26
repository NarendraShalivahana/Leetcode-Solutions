
class Solution:
    def minimumSteps(self, s: str) -> int:
        nums=[];fl=0
        for i in range(len(s)):
            if fl==1 and s[i]=="0":
                nums.append(i)
            elif s[i]=="1":
                fl=1
        nums=nums[::-1]
        res=0
        s=[int(i) for i in s]
        for i in range(len(s)):
            if nums and  s[i]==1:
                res+=(nums[-1]-i)
                s[i],s[nums.pop()]=0,1
        return res
        
