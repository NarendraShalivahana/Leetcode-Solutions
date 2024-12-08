class Solution:
    def minMoves2(self, beans: List[int]) -> int:
        beans.sort()
        n=len(beans)
        pos=[0 for _ in range(n)]
        pos.append(0)
        cur=0
        for i in range(n-1,-1,-1):
            cur+=beans[i]
            pos[i]=cur
        
        cur=0
        mini=float('inf')
        for i in range(n):
            num=beans[i]
            cnt1=(num*i)-cur
            cnt2=pos[i+1]-(num*(n-(i+1)))
            mini=min(mini,cnt1+cnt2)
            cur+=num
            # print(num,cnt1,cnt2)
        return mini
