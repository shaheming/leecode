#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len = len(s)
        max_sub_str_len = 0
        index = 0
        while index < str_len - max_sub_str_len:
            str_set = set()
            for item in s[index:]:
                if item in str_set:
                    break
                else:
                    str_set.add(item)
            set_len = len(str_set)
            max_sub_str_len = set_len if set_len > max_sub_str_len else max_sub_str_len
            index += 1
        return max_sub_str_len


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("aab"))
