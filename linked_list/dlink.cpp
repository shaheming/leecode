#include <cstdio>
const int g_kSize = 100000;
int left[g_kSize + 5], right[g_kSize + 5];
void Link(int l, int r);
int main()
{
  int n = 0, m = 0, kase = 0;
  while (std::scanf("%d %d", &n, &m) != EOF)
  {
    left[n + 1] = n;
    right[0] = 1;
    for (int i = 1; i <= n; ++i)
    {
      left[i] = i - 1;
      right[i] = i + 1;
    }
    int command = 0, x = 0, y = 0;
    bool reverse = false;
    while (m--)
    {
      std::scanf("%d", &command);
      if (command == 4)
      {
        reverse = !reverse;
      }
      else
      {
        std::scanf("%d %d", &x, &y);
        if (reverse && (command == 1 || command == 2))
        {
          command = 3 - command;
        }
        if (command == 1 && left[y] != x)
        {
          Link(left[x], right[x]);
          Link(left[y], x);
          Link(x, y);
        }
        else if (command == 2 && right[y] != x)
        {
          Link(left[x], right[x]);
          Link(x, right[y]);
          Link(y, x);
        }
        else if (command == 3)
        {
          int l_y = left[y], r_y = right[y], l_x = left[x], r_x = right[x];
          if (l_x != y)
          {
            Link(l_x, y);
            Link(x, r_y);
          }
          else
          {
            Link(x, y);
          }
          if (l_y != x)
          {
            Link(l_y, x);
            Link(y, r_x);
          }
          else
          {
            Link(y, x);
          }
        }
      }
    }
    int cur = (reverse ? left[n + 1] : right[0]);
    long long ans = 0;
    ans = ans + cur;
    for (int i = 2; i <= n; ++i)
    {
      cur = (reverse ? left[cur] : right[cur]);
      if (i % 2 == 1)
      {
        ans = ans + cur;
      }
    }
    std::printf("Case %d: %lld\n", ++kase, ans);
  }
  return 0;
}
void Link(int l, int r)
{
  right[l] = r;
  left[r] = l;
}