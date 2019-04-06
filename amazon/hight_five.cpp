

// There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.
// 给出一系列学生分数，求出每个学生最高的5门分数的平均分。
// Example:
// Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
// Return

#include <vector>
#include <unordered_map>
#include <iostream>
#include <climits>
#include <string>
#include <queue>
using namespace std;
class Solution
{
  typedef priority_queue<int, vector<int>, greater<int>> HQ;
  typedef unordered_map<int, HQ> DMAP;

public:
  vector<pair<int, double>> hight_five(vector<vector<int>> &data)
  {
    DMAP map;
    for (auto &d : data)
    {
      if (map.find(d[0]) == map.end())
      {
        map[d[0]] = HQ(); //注意typedef 这个怎么声明
        map[d[0]].push(d[1]);
      }
      else
      {
        map[d[0]].push(d[1]);
        while (map[d[0]].size() > 5)
          map[d[0]].pop();
      }
    }
    vector<pair<int, double>> r;
    double sum = 0;
    int cnt = 0;
    for (auto &item : map)
    {
      auto &p = item.second;
      cnt = 0;
      sum = 0;
      while (p.size() > 0)
      {
        cnt++;
        sum += p.top();
        p.pop();
      }
      r.push_back({item.first, sum / cnt});
    }
    return r;
  }
};

int main()
{
  vector<vector<int>> data = {
      {1, 91},
      {1, 92},
      {2, 93},
      {2, 99},
      {2, 98},
      {2, 97},
      {1, 60},
      {1, 58},
      {2, 100},
      {1, 61},
      {2, 100},
      {2, 100}};
  Solution s;
  vector<pair<int, double>> r = s.hight_five(data);
  for (auto &p : r)
  {
    cout << p.first << " " << p.second << endl;
  }
  return 0;
}