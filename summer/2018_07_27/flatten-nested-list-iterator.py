# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def flatten(nestedList):
            if nestedList.isInteger():
                return [nestedList.getInteger()]
            else:
                r = []
                for nl in nestedList.getList():
                    r+=flatten(nl)
                return r

        self.list = []
        for nl in nestedList:
            self.list +=  flatten(nl)
        self.length = len(self.list)
        self.index = 0


    def next(self):
        """
        :rtype: int
        """
        r = self.list[self.index]
        self.index += 1
        return r


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.length > self.index


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())