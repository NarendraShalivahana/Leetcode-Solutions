495.Teemo_Attacking
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        postime=-1
        cnt=0
        for i in timeSeries:
            # postime=(i+duration-1)
            if postime>=i:
                cur=postime-i+1
                cnt+=(duration-cur)
            else:
                cnt+=duration
            postime=(i+duration-1)
        return cnt

            

# 1 2
# 2

# 1- 1 2 pos 1+1=2
# 2- 2 3 pos.
