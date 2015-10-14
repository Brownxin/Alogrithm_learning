__author__ = 'Brown'
class PeekingIterator(object):
    def __init__(self,iterator):
        self.iterator=iterator
        self.peekFlag=False
        self.nextNum=None
    def peek(self):
        if not self.peekFlag:
            self.nextNum=self.iterator.next()
            self.peekFlag=True
        return self.nextNum
    def next(self):
        if not self.peekFlag:
            return self.iterator.next()
        self.peekFlag=False
        res=self.nextNum
        self.nextNum=None
        return res
    def hasNext(self):
        return self.peekFlag or self.iterator.hasNext()