__author__ = 'Brown'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self,array):
        if len(array)==0: return None
        if len(array)==1:
            return TreeNode(array[0])
        mid=int(len(array)/2)
        root=TreeNode(array[mid])
        root.left=self.sortedArrayToBST(array[:mid])
        root.right=self.sortedArrayToBST(array[mid+1:])
        return root
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array=[]
        p=head
        while p!=None:
            array.append(p.val)
            p=p.next
        return self.sortedArrayToBST(array)

# Solution 1
# class Solution(object):
#     def getMid(self,head):
#         slow=fast=head
#         while fast!=None and fast.next!=None:
#             slow=slow.next
#             fast=fast.next.next
#         return slow
#
#     def sortedListToBST(self, head):
#         """
#         :type head: ListNode
#         :rtype: TreeNode
#         """
#         if head==None: return None
#         if head.next==None:
#             return TreeNode(head.val)
#         mid=self.getMid(head)
#         root=TreeNode(mid.val)
#         head1=head
#         head2=mid.next
#         mid.next=None
#         phead1=head1
#         while phead1.next.next!=None:
#             phead1=phead1.next
#         phead1.next=None
#         root.left=self.sortedListToBST(head1)
#         root.right=self.sortedListToBST(head2)
#         return root