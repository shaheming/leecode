class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes: return 0
        envelopes = sorted(envelopes, key=lambda en: (en[0], en[1]))
        print(envelopes)
        maxrolls = [0 for _ in envelopes]
        maxroll = 1
        maxrolls[0] = 1
        for i in range(1, len(envelopes)):
            maxrolls[i] = 1
            for j in range(i - 1, -1, -1):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    maxrolls[i] = max(maxrolls[i], maxrolls[j] + 1)
                    maxroll = max(maxroll, maxrolls[i])
                    break
        return maxroll


en = [[46,89],[50,53],[52,68],[72,45],[77,81]]
s = Solution()
print(s.maxEnvelopes(en))
