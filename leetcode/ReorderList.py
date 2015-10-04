__author__ = 'Brown'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# Solution 2
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None or head.next.next==None:
            return head
        slow=fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        head1=head
        head2=slow.next
        slow.next=None
        dummy=ListNode(0)
        dummy.next=head2
        phead2=dummy.next
        while phead2.next!=None:
            tmp=dummy.next
            dummy.next=phead2.next
            phead2.next=phead2.next.next
            dummy.next.next=tmp
        head2=dummy.next
        dummy.next=head1
        p=dummy
        phead2=head2
        phead1=head1
        while phead2!=None and phead1!=None:
            tmp1=phead1.next
            tmp2=phead2.next
            p.next=phead1
            phead1.next=phead2
            phead2.next=tmp1
            p=p.next.next
            phead1=tmp1
            phead2=tmp2
        if phead1: p.next=phead1
        if phead2: p.next=phead2
        head=dummy.next

# Solution 1
# class Solution(object):
#     def reorderList(self, head):
#         """
#         :type head: ListNode
#         :rtype: void Do not return anything, modify head in-place instead.
#         """
#         if head==None or head.next==None or head.next.next==None:
#             head=head
#         else:
#             slow=fast=head
#             while fast!=None and fast.next!=None:
#                 slow=slow.next
#                 fast=fast.next.next
#             head1=head
#             head2=slow.next
#             slow.next=None
#
#             dummy=ListNode(0)
#             dummy.next=head2
#             phead2=dummy.next
#             while phead2.next!=None:
#                 tmp=dummy.next
#                 dummy.next=phead2.next
#                 phead2.next=phead2.next.next
#                 dummy.next.next=tmp
#             head2=dummy.next
#
#             phead2=head2
#             phead1=head1
#             while phead2!=None:
#                 tmp1=phead1.next
#                 tmp2=phead2.next
#                 phead1.next=phead2
#                 phead2.next=tmp1
#                 phead1=tmp1
#                 phead2=tmp2