class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == '': return True
        if len(s2) < len(s1): return False
        dct1 = {}
        dct2 = {}

        for i in range(len(s1)):
            if s1[i] in dct1:
                dct1[s1[i]] += 1
            else:
                dct1[s1[i]] = 1
            if s2[i] in dct2:
                dct2[s2[i]] += 1
            else:
                dct2[s2[i]] = 1

        if dct1 == dct2:
            return True
        index = 0
        for s in s2[len(s1):]:
            dct2[s2[index]] -= 1
            if dct2[s2[index]] == 0:
                del dct2[s2[index]]
            if s in dct2:
                dct2[s] += 1
            else:
                dct2[s] = 1
            if dct1 == dct2:
                return True
            index += 1
        return False

    # 用 array 代替 hash 来进行对比
    def checkInclusion2(self, s1, s2):
        A = [ord(s) - ord('a') for s in s1]
        B = [ord(s) - ord('a') for s in s2]
        taget = [0] * 26
        window = [0] * 26
        for s in A:
            taget[s] += 1
        for s in B:
            window[s] += 1
        for i in range(len(s2)):
            if i >= len(s1):
                if window == taget:
                    return True
                window[B[i - len(s1)]] -= 1
                window[B[i]] += 1
        return False
