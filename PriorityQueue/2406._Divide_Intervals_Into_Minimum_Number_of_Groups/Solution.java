class Solution {
    public int minGroups(int[][] intervals) {
        PriorityQueue<Integer> pq=new PriorityQueue<>();
        Arrays.sort(intervals,(a,b)-> Integer.compare(a[0],b[0]));

        for(int i=0;i<intervals.length;i++){
            if(!pq.isEmpty() && pq.peek()<intervals[i][0]){
                pq.poll();
            }
            pq.offer(intervals[i][1]);
        }
        return pq.size();
    }
}
