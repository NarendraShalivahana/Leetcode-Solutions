class Solution:
    def maximumSwap(self, num: int) -> int:
        n=[i for i in str(num)]
        for i in range(len(n)-1):
            cur="-1"
            ind=-1
            for j in range(i+1,len(n)):
                if n[i]<n[j]:
                    cur=max(cur,n[j])
                    if cur==n[j]:
                        ind=max(ind,j)
            if cur!="-1":
                n[i],n[ind]=n[ind],n[i]
                ans=""
                for i in n:
                    ans+=i
                return int(ans)
        return num
        
