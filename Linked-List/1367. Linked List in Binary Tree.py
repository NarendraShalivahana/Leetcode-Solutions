QUESTION:
https://leetcode.com/problems/linked-list-in-binary-tree/description/?envType=daily-question&envId=2024-09-07

SOLUTION:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def f(root,head):
            if root==None:
                if head==None:
                    return True
                return False
            if head==None:
                return True
            return (head.val==root.val) and (f(root.left,head.next) or f(root.right,head.next))

        def fl(root):
            if root==None:
                return False
            if f(root,head)==True:
                return True
            
            return fl(root.left) or fl(root.right)
        ans=fl(root)
        return ans



