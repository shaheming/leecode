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
  vector<int> findOrder(int numCourses, vector<pair<int, int>> &prerequisites)
  {
    if (numCourses == 0)
      return vector<int>();

    vector<vector<int>> graph(numCourses, vector<int>());
    unordered_map<int, int> visted;
    vector<int> du(numCourses, 0);

    for (auto &p : prerequisites)
    {
      graph[p.second].push_back(p.first);
      du[p.first]++;
    }

    queue<int> q;
    vector<int> r;
    for (int i = 0; i < du.size(); i++)
    {
      if (du[i] == 0)
      {
        q.push(i);
      }
    }
    while (!q.empty())
    {
      int c = q.front();
      visted[c] = 1;
      for (auto &child : graph[c])
      {
        du[child]--;
        if (du[child] == 0 && visted.find(child) == visted.end())
        {
          q.push(child);
        }
      }
      r.push_back(c);
      q.pop();
    }

    if (r.size() != numCourses)
      return vector<int>();
    else
      return r;
  }
};