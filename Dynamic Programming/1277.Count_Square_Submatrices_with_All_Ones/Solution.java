1277.Count_Square_Submatrices_with_All_Ones
class Solution {
    public int countSquares(int[][] mat) {
        int n=mat.length;
        int m=mat[0].length;
        int ans=0;
        for(int i=1;i<n;i++){
            for(int j=1;j<m;j++){
                if(mat[i][j]==1){
                    int temp=Math.min(mat[i-1][j-1],mat[i-1][j]);
                    mat[i][j]=1+Math.min(temp,mat[i][j-1]);
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                ans+=mat[i][j];
            }
        }
        return ans;
    }
}
