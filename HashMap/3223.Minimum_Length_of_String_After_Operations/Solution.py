3223.Minimum_Length_of_String_After_Operations
class Solution {
    public int minimumLength(String s) {
        int[] arr=new int[26];
        for(int i=0;i<s.length();i++){
            int ind=s.charAt(i)-97;
            arr[ind]+=1;
        }
        int res=0;
        for(int i:arr){
            System.out.print(i);
            if(i>0){
                res+=1;
                i-=1;
                res+=(i%2);
            }
        }
        return res;
        
    }
}
