//Substring with K Distinct Chars I(return no size limit)
// https: //www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/

// Count number of substrings with exactly k distinct characters
//     Given a string of lowercase alphabets,
//     count all possible substrings(not necessarily distinct) that has exactly k distinct characters.Examples :

//     Input : abc,
//     k = 2 Output : 2 Possible substrings are{"ab", "bc"}

//     Input : aba,
//     k = 2 Output : 3 Possible substrings are{"ab", "ba", "aba"}

//     Input : aa,
//     k = 1 Output : 3 Possible substrings are
// { "a", "a", "aa"}

#include <vector>
#include <unordered_map>
#include <iostream>
#include <climits>
#include <string>
using namespace std;

class Solution
{
public:
  int kdistinct(string s, int k)
  {
    if (s.size() == 0 || k == 0 || k > 26)
      return 0;
    unordered_map<string, int> wordsSet;
    unordered_map<char, int> charSet;
    for (int i = 0; i < s.size(); i++)
    {
      // int bound = (i + k > s.size()) ? s.size() : i + k;// if you want exactly k
      int bound = s.size();
      for (int j = i; j < bound; j++)
      {
        if (charSet.size() == k && charSet.find(s[j]) == charSet.end())
        {
          break;
        }
        else
        {
          charSet[s[j]]++;
          if (charSet.size() == k)
          {
            wordsSet[s.substr(i, j - i + 1)]++; //note j - i + 1
          }
        }
      }
      charSet.clear();//note easy to miss
    }
    return wordsSet.size();
  }
};
int main()
{
  string str = "aaaaaab";
  Solution s = Solution();
  cout << s.kdistinct(str, 2);
  return 0;
}
