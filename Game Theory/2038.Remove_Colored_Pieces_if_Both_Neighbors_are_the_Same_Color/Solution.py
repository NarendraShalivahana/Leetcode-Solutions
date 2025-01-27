2038.Remove_Colored_Pieces_if_Both_Neighbors_are_the_Same_Color
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n=len(colors)
        a=[]
        cur=colors[0]
        for i in range(1,n):
            if cur[-1]!=colors[i]:
                a.append(cur)
                cur=colors[i]
            else:
                cur+=cur[-1]
        a.append(cur)
        A,B=0,0
        for i in a:
            if i[0]=="A":
                A+=len(i)-2 if len(i)>2 else 0
            else:
                B+=len(i)-2 if len(i)>2 else 0
        if A>B:
            return True
        else:
            return False

        
