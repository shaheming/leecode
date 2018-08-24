import collections

#bfs搜索，用条件减少搜索量
#主要tuple 与 set queue 的组合需要 [(1,2)]
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        result = [[0 for _ in range(col)] for _ in range(row)]
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(row):
            for c in range(col):
                if matrix[r][c] != 0:
                    queue = collections.deque([(r, c)])
                    visited = set([(r, c)])
                    min_length = row + col
                    while queue:
                        tmp_r, tmp_c = queue.popleft()
                        for i, j in direction:
                            if tmp_c + j >= 0 and tmp_c + j < col and tmp_r + i >= 0 and tmp_r + i < row \
                                    and abs(tmp_r + i - r) + abs(tmp_c + j - c) < min_length:
                                if matrix[tmp_r + i][tmp_c + j] == 0:
                                    min_length = min([abs(tmp_r + i - r) + abs(tmp_c + j - c), min_length])
                                else:
                                    if (tmp_r + i, tmp_c + j) not in visited:
                                        queue.append((tmp_r + i, tmp_c + j))
                                        visited.add((tmp_r + i, tmp_c + j))
                    result[r][c] = min_length
        return result
