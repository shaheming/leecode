# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
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

    # 如何改进呢？改进的方法是通过分析有哪些重复计算。
    # 例如我们已经证明的 Sij 是一个没有重复的子串，那么我们就不需要再从这个子串里面开始找了Sij
    # 这里的核心思想是去除了重复计算
    def lengthOfLongestSubstring2(self, s):
        str_len = len(s)
        max_sub_str_len = 0
        i = j = 0
        end_index = str_len - max_sub_str_len
        str_set = set()
        while i < end_index and j < end_index:
            if s[j] not in str_set:
                str_set.add(s[j])
                max_sub_str_len = max([max_sub_str_len, len(str_set)])
                j += 1
            else:
                str_set.remove(s[i])
                i += 1
        return max_sub_str_len


s = Solution()
print(s.lengthOfLongestSubstring2("abcabcbb"))
print(s.lengthOfLongestSubstring2("bbbbb"))
print(s.lengthOfLongestSubstring2("aab"))
