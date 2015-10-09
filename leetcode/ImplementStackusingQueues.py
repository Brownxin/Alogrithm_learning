__author__ = 'Brown'
class Stack(object):
    def __init__(self):
        self.queue=[]

    def push(self,x):
        self.queue.append(x)

    def pop(self):
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
        self.queue.pop(0)

    def top(self):
        for i in range(len(self.queue)):
            top=self.queue[0]
            self.queue.append(self.queue.pop(0))
        return top

    def empty(self):
        return len(self.queue)==0