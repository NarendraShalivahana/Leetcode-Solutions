2364.Count_Number_of_Bad_Pairs
class Solution {
    public long countBadPairs(int[] nums) {
        long n=nums.length;
        long nop=n*(n-1)/2;
        long cur;
        long count=0;
        Map<Long,Long> map=new HashMap<>();
        for(int i=0;i<n;i++){
            cur=nums[i]-i;
            if(map.containsKey(cur)){
                count+=map.get(cur);
            }
            map.put((long)cur,map.getOrDefault(cur,0L)+1L);
            
        }
        return nop-count;
        
    }
}
