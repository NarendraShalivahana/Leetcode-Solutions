2657.Find_the_Prefix_Common_Array_of_Two_Arrays
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        c=[0 for _ in range(n)]
        d=dict()
        cnt=0
        for i in range(n):
            d[A[i]]=1
            d[B[i]]=1
            cnt+=2
            cur=cnt-len(d)
            c[i]=cur
            
            
        return c
                
        
        
