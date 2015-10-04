__author__ = 'Brown'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head==None:
            return None
        length=n-m
        dummy=ListNode(0)
        dummy.next=head
        start=dummy
        while m>1:
            start=start.next
            m-=1
        p=start.next
        while length>0:
            tmp=start.next
            start.next=p.next
            p.next=p.next.next
            start.next.next=tmp
            length-=1
        return dummy.next