__author__ = 'Brown'
class TreeNode():
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return None
        slow=fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if slow==fast:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
        return None