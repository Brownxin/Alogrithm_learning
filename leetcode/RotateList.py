__author__ = 'Brown'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or k==0:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        count=0
        while p.next!=None:
            p=p.next
            count+=1
        step=count-(k%count)
        p=dummy
        for i in range(step):
            p=p.next
        head=p.next
        p.next=None
        return head