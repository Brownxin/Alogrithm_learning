__author__ = 'Brown'
# Definition for singly-linked list.
class ListNode():
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        cur=head
        while cur.next!=None:
            if cur.val>cur.next.val:
                pre=dummy
                while pre.next.val<cur.next.val:
                    pre=pre.next
                tmp=cur.next
                cur.next=tmp.next
                tmp.next=pre.next
                pre.next=tmp
            else:
                cur=cur.next
        return dummy.next
