1800.Maximum_Ascending_Subarray_Sum
class Solution {
    public int maxAscendingSum(int[] nums) {
        int res=0;
        int cur=nums[0];
        for(int i=1;i<nums.length;i++){
            if(nums[i-1]<nums[i]){
                cur+=nums[i];
            }else{
                res=Math.max(cur,res);
                cur=nums[i];
            }
        }
        res=Math.max(res,cur);
        return res;
    }
}
