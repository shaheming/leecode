#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

struct Cmp
{
  bool operator()(const pair<int, int> &p1, const pair<int, int> &p2) const
  {
    if (p1.first == p2.first)
      return p1.second < p2.second;
    else
      return p1.first < p2.first;
  }
};

class Solution
{
public:
  bool maxSlidingWindow(vector<int> &nums, int k, double allowedIncrease)
  {
    //Monotonic queue
    deque<int> dq;
    vector<int> maxIndexes;
    vector<double> avgs;
    double sum = 0;

    //find maxIndexes and average in each sliding windows
    //using the monotonic queue find the maxIndexes in the windows with O(n)
    //stores inputsIndex, because there may be duplicate elements
    for (int i = 0; i < nums.size(); i++)
    {
      while (!dq.empty() && nums[dq.back()] < nums[i])
        dq.pop_back();
      dq.push_back(i);
      sum += nums[i];
      if (i >= k - 1)
      {
        avgs.push_back(sum / k);
        sum -= nums[i - k + 1];
        maxIndexes.push_back(dq.front());
        if (i - k + 1 == dq.front())
          dq.pop_front();
      }
    }
    //find the sliding windows started at i which contain the maxIndexes[]
    unordered_map<int, vector<int>> map;
    for (int i; i < nums.size() - k + 1; i++)
    {
      int maxIndex = maxIndexes[i];
      double avg = avgs[i];
      map[maxIndex].push_back(avg);
    }
    for (auto &item : map)
    {
      int maxVal = nums[item.first];
      auto v = item.second;
      if ((maxVal / allowedIncrease) >= *max_element(v.begin(), v.end()))
      {
        return true;
      }
    }

    for (auto it = avgs.begin() + 1; it != avgs.end(); it++)
    {
      if (*(it - 1) * allowedIncrease <= *(it))
        return true;
    }

    return false;
  }
};
int findALD(int year)
{
  const int startYear = 1970;
  const int startWeekDay = 4;
  const int daysBeforeOtc = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30;
  int years = year - startYear;

  //cal days between
  int daysBeforeYear = years * 365 + years / 4 - years / 100 + years / 400;
  int weekDayAtOct = (daysBeforeYear + daysBeforeOtc + startWeekDay) % 7;
  int day = 0;

  //deal with the day before 1970
  if (weekDayAtOct < 0)
    weekDayAtOct += 7;

  if (weekDayAtOct > 2)
  {
    day = 14 + 1 - (weekDayAtOct - 2);
  }
  else
  {
    day = 7 + 1 + (2 - weekDayAtOct);
  }
  return day;
}
int main()
{
  // Solution s;
  // vector<int> nums = {99, 100, 1, 1000, 2};
  // bool r = s.maxSlidingWindow(nums, 3, 2);
  // if (r)
  //   cout << "true";
  // else
  // {
  //   cout << "False";
  // }
  cout << findALD(2017);
  return 0;
}

// write a function to cal the date between of year/otc
