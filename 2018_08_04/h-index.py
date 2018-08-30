class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0: return 0
        citations = sorted(citations)
        max_c = 0
        for index in range(len(citations) - 1, -1, -1):
            for i in range(min(len(citations), citations[index]), -1, -1):
                if len(citations) - index >= i and citations[index] >= i:
                    max_c = max(max_c, i)
                    break
        return max_c
