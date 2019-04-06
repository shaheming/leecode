class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        map2 = {"I": {"V", "X"}, "X": {"L", "C"}, "C": {"D", "M"}}
        result = 0
        index = 0
        while index < len(s):
            if index + 1 < len(s) and s[index] in map2 and s[index + 1] in map2[s[index]]:
                result += num_map[s[index + 1]] - num_map[s[index]]
                index += 1
            else:
                result += num_map[s[index]]
            index += 1
        return result
