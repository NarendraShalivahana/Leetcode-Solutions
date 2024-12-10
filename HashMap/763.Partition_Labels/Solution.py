763.Partition_Labels
class Solution(object):
    def partitionLabels(self, S):
        Map={}
        for i,e in enumerate(S):
            Map[e]=i
        eleindex=0
        size=0
        res=[]
        for i,ele in enumerate(S):
            eleindex=max(eleindex,Map[ele])
            size+=1
            if i==eleindex:
                res.append(size)
                size=0               
        return res
                
