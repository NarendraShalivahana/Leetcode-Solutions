2.Add_Two_Numbers

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode cur1=l1;
        ListNode cur2=l2;
        int count=0;
        ListNode head=new ListNode(0);
        ListNode poi=head;
        while (cur1!=null || cur2!=null || count!=0){
            if (cur1!=null){
                count+=cur1.val;
                cur1=cur1.next;
            }
            if(cur2!=null){
                count+=cur2.val;
                cur2=cur2.next;
            }
            //System.out.print(count+" ");
            poi.next=new ListNode(count%10);
            poi=poi.next;
            //System.out.print(poi.val+" ");
            count=count/10;
            //System.out.print(count+" \\");
            
            
        }
        return head.next;
    }
}
