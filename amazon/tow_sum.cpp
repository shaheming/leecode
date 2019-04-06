#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution
{
public:
  /**
     * @param numbers: An array of Integer
     * @param target: target = numbers[index1] + numbers[index2]
     * @return: [index1, index2] (index1 < index2)
     */
  vector<int> twoSum(vector<int> &numbers, int target)
  {
    unordered_map<int, int> map;
    int index = 0;
    vector<int> r;
    for (auto &n : numbers)
    {
      if (map.find(target - n) != map.end())
      {
        r.push_back(index);
        r.push_back(map[target - n]);
        break;
      }
      else
      {
        map[n] = index;
      }
      index++;
    }

    sort(r.begin(), r.end());
    return r;
  }
};