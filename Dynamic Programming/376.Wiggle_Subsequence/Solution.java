376.Wiggle_Subsequence
class Solution {
    public int wiggleMaxLength(int[] nums) {
        int n=nums.length;
        int[] pos=new int[n];
        int[] neg=new int[n];
        Arrays.fill(pos,1);
        Arrays.fill(neg,1);
        int res=1;
        int cur;
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                cur=nums[j]-nums[i];
                if(cur>0){
                    pos[i]=Math.max(pos[i],1+neg[j]);
                    res=Math.max(res,pos[i]);
                }
                else if(cur<0){
                    neg[i]=Math.max(neg[i],1+pos[j]);
                    res=Math.max(res,neg[i]);
                }

            }
        }
        return res;
        
    }
}
