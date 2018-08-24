#这个问题本来是一个 O(N^4) 但是通过拆解可以拆解为两个 O(2*N^2) 的问题

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        dicA, dicB, dicC, dicD = {}, {}, {}, {}
        for a in A:
            for b in B:
                if a + b in dicA:
                    dicA[a + b] += 1
                else:
                    dicA[a + b] = 1
        for c in C:
            for d in D:
                if -(c + d) in dicA:
                    count += dicA[-(c + d)]
        return count
