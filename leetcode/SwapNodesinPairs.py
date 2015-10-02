__author__ = 'Brown'
# Definition for singly-linked list.
class TreeNode():
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Solution 1
        if head==None or head.next==None:
            return head
        dummy=TreeNode(0)
        dummy.next=head
        node=dummy
        while node.next!=None and node.next.next!=None:
            pre,post=node.next,node.next.next
            pre.next=post.next
            post.next=pre
            node.next=post
            node=pre
        return dummy.next

    # Solution 2
    # if head==None or head.next==None:
    #         return head
    #     dummy=TreeNode(0)
    #     dummy.next=head
    #     node=dummy
    #     while node.next!=None and node.next.next!=None:
    #         tmp=node.next.next
    #         node.next.next=tmp.next
    #         tmp.next=node.next
    #         node.next=tmp
    #         node=tmp.next
    #
    #     return dummy.next
