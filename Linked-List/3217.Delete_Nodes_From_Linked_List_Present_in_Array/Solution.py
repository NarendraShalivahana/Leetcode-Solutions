# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        d=dict()
        for i in nums:
            d[i]=1
        cur=head
        while cur and cur.next:
            temp=cur.next
            while temp and d.get(temp.val,0)==1:
                temp=temp.next
            cur.next=temp
            cur=cur.next
        if d.get(head.val,0)==1:
            head=head.next
        return head
