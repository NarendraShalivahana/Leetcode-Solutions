1406.Stone_Game_III
class Solution {
    public String stoneGameIII(int[] st) {
        int n=st.length;
        int[] dp=new int[n+1];
        Arrays.fill(dp,Integer.MAX_VALUE);
        int ans=f(0,st,dp,n);
        if(ans==0){
            return "Tie";
        }
        else if(ans>0){
            return "Alice";
        }
        return "Bob";
        
    }
    int f(int pos,int[] st,int[] dp,int n){
        if (pos>=n){
            return 0;
        }
        if(dp[pos]!=Integer.MAX_VALUE){
            return dp[pos];
        }
        int s=0;
        int res=Integer.MIN_VALUE;
        for(int i=pos;i<Math.min(n,pos+3);i++){
            s+=st[i];
            res=Math.max(res,s-f(i+1,st,dp,n));
        }
        dp[pos]=res;
        return res;
    }
}
