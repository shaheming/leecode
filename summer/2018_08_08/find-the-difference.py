class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        arrayA = [0 for _ in range(26)]
        arrayB = [0 for _ in range(26)]
        for i in s:
            arrayA[ord(i) - ord('a')] += 1
        for i in t:
            arrayB[ord(i) - ord('a')] += 1
        r = set()

        for i,d in enumerate(zip(arrayA,arrayB)):
            if d[1]- d[0]  > 0:
                r.add(chr(ord('a') + i))
        return "".join(list(r))


sorted([(1, 2), (2, 3)], key=lambda x: x[0])
