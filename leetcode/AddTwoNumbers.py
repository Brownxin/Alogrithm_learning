__author__ = 'Brown'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l1
        if l2==None:
            return l2
        dummy=ListNode(0)
        p=dummy
        flag=0
        while l1!=None and l2!=None:
            p.next=ListNode((l1.val+l2.val+flag)%10)
            flag=int((l1.val+l2.val+flag)/10)
            l1=l1.next
            l2=l2.next
            p=p.next
        if l2!=None:
            while l2!=None:
                p.next=ListNode((l2.val+flag)%10)
                flag=int((l2.val+flag)/10)
                p=p.next
                l2=l2.next
        if l1!=None:
            while l1!=None:
                p.next=ListNode((l1.val+flag)%10)
                flag=int((l1.val+flag)/10)
                p=p.next
                l1=l1.next
        if flag!=0: p.next=ListNode(flag)
        return dummy.next