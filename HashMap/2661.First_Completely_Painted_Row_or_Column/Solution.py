2661.First_Completely_Painted_Row_or_Column
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n,m=len(mat),len(mat[0])
        d1,d2=dict(),dict()
        s=len(arr)
        res=None
        d=dict()
        for i in range(n):
            for j in range(m):
                d[mat[i][j]]=[i,j]
        
        for i in range(s):
            a,b=d.get(arr[i])
            d1[a]=d1.get(a,0)+1
            d2[b]=d2.get(b,0)+1
            if d1[a]==m:
                return i
            if d2[b]==n:
                return i
                
            
        
