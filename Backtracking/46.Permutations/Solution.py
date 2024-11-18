class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def f(vis,path,res,n):
            if False not in vis:
                res.append(path.copy())
                return

            for i in range(n):
                if vis[i]==False:
                    vis[i]=True
                    path.append(nums[i])
                    f(vis,path,res,n)
                    path.pop()
                    vis[i]=False
            
            return

        res=[]
        n=len(nums);vis=[False for _ in range(n)]
        f(vis,[],res,n)
        return res
