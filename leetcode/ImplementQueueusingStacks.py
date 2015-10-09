__author__ = 'Brown'

# Solution 2------Using One Stack
class Queue(object):
    def __init__(self):
        self.stack=[]

    def push(self,x):
        swap=[]
        while self.stack:
            swap.append(self.stack.pop())
        swap.append(x)
        while swap:
            self.stack.append(swap.pop())

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack)==0

# Solution 1----Using Two Stacks
# class Queue(object):
#     def __init__(self):
#         self.in_stack=[]
#         self.out_stack=[]
#
#     def push(self,x):
#         self.in_stack.append(x)
#
#     def pop(self):
#         self.peek()
#         self.out_stack.pop()
#
#     def peek(self):
#         if not self.out_stack:
#             while self.in_stack:
#                 self.out_stack.append(self.in_stack.pop())
#         return self.out_stack[-1]
#
#     def empty(self):
#         return len(self.in_stack)+len(self.out_stack)==0