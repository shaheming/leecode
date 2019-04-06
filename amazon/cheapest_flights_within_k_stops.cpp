//https://leetcode.com/problems/cheapest-flights-within-k-stops/

#include <vector>
#include <unordered_map>
#include <iostream>
#include <climits>
#include <string>
#include <queue>
using namespace std;

// class Solution
// {
// public:
//   int findCheapestPrice(int n, vector<vector<int>> &flights, int src, int dst, int K)
//   {
//     if (flights.size() == 0)
//       return -1;

//     vector<vector<pair<int, int>>> graph(n, vector<pair<int, int>>());
//     queue<pair<int, int>> dp;
//     for (auto &f : flights)
//       graph[f[0]].push_back({f[1], f[2]});
//     int hop = 0;
//     dp.push({src, 0});
//     int price_sum = 0;
//     int ans = INT_MAX;
//     while (dp.size() > 0 && hop <= K)
//     {
//       int len = dp.size();
//       for (int i = 0; i < len; i++)
//       {
//         auto flight = dp.front();
//         dp.pop();
//         if (flight.first == dst)
//           ans = min(ans, flight.second);
//         for (auto &f : graph[flight.first])
//         {
//           if (flight.second + f.second < ans)
//           {
//             dp.push({f.first, flight.second + f.second});
//           }
//         }
//       }
//       hop++;
//     }
//     if (ans == INT_MAX)
//       return -1;
//     else
//       return ans;
//   }
// };
class Solution
{
public:
  int findCheapestPrice(int n, vector<vector<int>> &flights, int src, int dst, int K)
  {

    int INF = 10000 * 100; //要注意这个数字的选择，不要overflow了int的大小 2**31 -1
    vector<vector<int>> dp(K + 2, vector<int>(n, INF));

    dp[0][src] = 0;
    for (int i = 1; i <= K + 1; i++)
    {
      dp[i][src] = 0;

      for (auto &f : flights)
      {
        dp[i][f[1]] = min(dp[i][f[1]], dp[i - 1][f[0]] + f[2]);
      }
    }

    return dp[K + 1][dst] >= INF ? -1 : dp[K + 1][dst];
  }
};
int main()
{
  vector<vector<int>> v = {{0, 1, 100},
                           {1, 2, 100},
                           {0, 2, 500}};
  for (auto &i : v)
  {
    for (auto &j : i)
      cout << j << ' ';
    cout << endl;
  }
  Solution s;
  cout << s.findCheapestPrice(3, v, 0, 2, 2) << endl;
  cout << pow(2, 2) << endl;
  return 0;
}