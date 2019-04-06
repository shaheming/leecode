//https: //leetcode.com/problems/longest-palindromic-substring/submissions/
#include <vector>
#include <unordered_map>
#include <iostream>
#include <climits>
#include <string>
#include <queue>
using namespace std;

class Solution
{
public:
  string longestPalindrome(string s)
  {
    if (s.size() == 0)
      return "";
    int mid = 0, left = 0, right = 0;
    int max_len = 0;
    int max_start = 0;
    while (mid < s.size())
    {
      left = right = mid;
      while (right + 1 < s.size() && s[right] == s[right + 1])
        right++;
      mid = right + 1;
      while (left - 1 >= 0 && right + 1 < s.size() && s[left - 1] == s[right + 1])
      {
        left--;
        right++;
      }
      if (right - left + 1 > max_len)
      {
        max_len = right - left + 1;
        max_start = left;
      }
    }
    return s.substr(max_start, max_len);
  }
};