class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        left, center, right = 0, 0, 0
        counter = 0
        while center < len(s):
            counter += 1
            left, right = center - 1, center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    counter += 1
                    left -= 1
                    right += 1

            left, right = center - 1, center+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    counter += 1
                    left -= 1
                    right += 1
            center += 1
        return counter
