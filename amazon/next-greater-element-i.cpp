// https : //leetcode.com/problems/next-greater-element-i/submissions/
class Solution
{
public:
  vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
  {
    vector<int> r;
    if (nums1.size() == 0)
      return r;

    unordered_map<int, int> map;
    stack<int> s;
    for (auto &n : nums2)
    {
      while (!s.empty() && s.top() < n)
      {
        map[s.top()] = n;
        s.pop();
      }
      s.push(n);
    }
    while (!s.empty())
    {
      map[s.top()] = -1;
      s.pop();
    }

    for (auto &n : nums1)
      r.push_back(map[n]);

    return r;
  }
};