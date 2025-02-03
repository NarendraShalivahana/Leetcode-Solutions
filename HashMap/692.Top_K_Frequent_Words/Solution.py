692.Top_K_Frequent_Words
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        words.sort()
        c=Counter(words)
        count=0
        res=[]
        for i in c.most_common():
            res.append(i[0])
            count+=1
            if count==k:
                break
        #res.sort()
        return res
