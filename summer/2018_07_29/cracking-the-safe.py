class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k == 1: return '0' * n
        v = k ** (n - 1)
        visited = [[False for _ in range(k)] for _ in range(v)]
        sequence = []

        def dfs(n):
            for i in range(k):
                if not visited[n][i]:
                    visited[n][i] = True
                    dfs((n * k + i) % v)
                    sequence.append('0' + i)

        dfs(0)
        return "".join(sequence + sequence[:n - 1])
