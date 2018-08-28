class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        chMap = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w','x', 'y', 'z']}
        import collections
        q = collections.deque([])
        r = collections.deque([])
        for d in digits:q.append(chMap[int(d)])

        while q:
            chs = q.popleft()
            if not r:
                for i in chs:
                    r.append([i])
            else:

                for _ in range(len(r)):
                    a = r.popleft()
                    for c in chs:
                        tmp = [i for i in a] + [c]
                        r.append(tmp)

        return ["".join(l) for l in list(r)]


"aa".find()