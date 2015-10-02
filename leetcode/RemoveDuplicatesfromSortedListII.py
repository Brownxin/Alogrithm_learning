__author__ = 'Brown'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        tmp=dummy.next
        while p.next!=None:
            while tmp.next!=None and tmp.next.val==p.next.val:
                tmp=tmp.next
            if tmp==p.next:
                tmp=tmp.next
                p=p.next
            else:
                p.next=tmp.next
        return dummy.next

