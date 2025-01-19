93.Restore_IP_Addresses
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def f(pos,s,n,cnt,path,res):
            if pos>=n:
                if cnt==4:
                    res.add(path[:-1])
                return
            cur=""
            for i in range(pos,n):
                cur+=s[i]
                if s[pos]=="0":
                    f(pos+1,s,n,cnt+1,path+cur+".",res)
                    return
                elif cur[0]!="0" and 0<=int(cur)<=255:
                    f(i+1,s,n,cnt+1,path+cur+".",res)
                
                    
        res=set()
        f(0,s,len(s),0,"",res)
        return list(res)
        
            
