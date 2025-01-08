3042.Count_Prefix_and_Suffix_Pairs_I
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def f(a,b):
            n,m=len(a),len(b)
            if a==b[:n] and a==b[m-n:m]:
                return True
            # elif a[:m]==b and a[n-m:n]==b:
            #     return True
            return False
        
        
        
        n=len(words)
        cnt=0
        for i in range(n-1):
            for j in range(i+1,n):
                if f(words[i],words[j])==True:
                    cnt+=1
        return cnt
        
