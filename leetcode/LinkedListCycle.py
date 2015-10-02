__author__ = 'Brown'
# Definition for singly-linked list.
class TreeNode():
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None and head.next==None:
            return False
        slow=fast=head

        while fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False