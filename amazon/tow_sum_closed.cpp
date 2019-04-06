#include <vector>
#include <unordered_map>
#include <iostream>
#include <climits>
using namespace std;

class Solution
{
public:
  /**
     * @param numbers: An array of Integer
     * @param target: target = numbers[index1] + numbers[index2]
     * @return: [index1, index2] (index1 < index2)
     */

  int twoSumClosest(vector<int> &numbers, int target)
  {
    int diff = INT_MAX;
    sort(numbers.begin(), numbers.end());
    int l = 0, r = numbers.size() - 1;
    while (l < r)
    {

      if (target < numbers[l] + numbers[r])
      {
        diff = diff > numbers[l] + numbers[r] - target ? (numbers[l] + numbers[r] - target) : diff;
        r--;
      }
      else if (target == numbers[l] + numbers[r])
      {
        diff = 0;
        break;
      }
      else
      {
        diff = diff > target - numbers[l] - numbers[r] ? target - (numbers[l] + numbers[r]) : diff;
        
        l++;
      }
    }

    return diff;
  }
};

int main(){
  vector<int>nums = {-1, 2, 1, -4};
  Solution s = Solution();
  cout << s.twoSumClosest(nums, 4);
};