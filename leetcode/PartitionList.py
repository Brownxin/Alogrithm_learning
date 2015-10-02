__author__ = 'Brown'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        head1=ListNode(0)
        tmp1=head1
        head2=ListNode(0)
        tmp2=head2
        p=head
        while p!=None:
            if p.val<x:
                tmp1.next=p
                p=p.next
                tmp1=tmp1.next
                tmp1.next=None
            else:
                tmp2.next=p
                p=p.next
                tmp2=tmp2.next
                tmp2.next=None
        tmp1.next=head2.next
        return head1.next