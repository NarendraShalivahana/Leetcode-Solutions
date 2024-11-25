Geek's Training(GFG)
class Solution {
    public int maximumPoints(int arr[][], int N) {
        // code here
        int[][] dp=new int[N][3];
        int maxi=0;
        dp[0]=arr[0];
        for(int i=1;i<N;i++){
            for(int j=0;j<3;j++){
                if(j==0){
                    dp[i][j]=Math.max(dp[i-1][j+1],dp[i-1][j+2]);
                }
                else if(j==2){
                    dp[i][j]=Math.max(dp[i-1][j-1],dp[i-1][j-2]);
                }
                else{
                    dp[i][j]=Math.max(dp[i-1][j-1],dp[i-1][j+1]);
                }
                dp[i][j]+=arr[i][j];
                maxi=Math.max(maxi,dp[i][j]);
            }
        }return maxi;
    }
}
