2914.Minimum_Number_of_Changes_to_Make_Binary_String_Beautiful

class Solution:
    def minChanges(self, s: str) -> int:
        n=len(s);
        z,o=0,0
        res=0
        for i in range(n):
            if s[i]=="0":
                z+=1
            else:
                o+=1
            if i%2!=0:
                res+=min(z,o)
                z=0
                o=0
        return res
