__author__ = 'Brown'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge(self,head1,head2):
        if head1==None: return head2
        if head2==None: return head1
        dummy=ListNode(0)
        p=dummy
        while head1!=None and head2!=None:
            if head1.val<head2.val:
                p.next=head1
                head1=head1.next
                p=p.next
            else:
                p.next=head2
                head2=head2.next
                p=p.next
        if head2:
            p.next=head2
        if head1:
            p.next=head1
        return dummy.next
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        slow=head;fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        head1=head
        head2=slow.next
        slow.next=None
        head1=self.sortList(head1)
        head2=self.sortList(head2)
        head=self.merge(head1,head2)
        return head