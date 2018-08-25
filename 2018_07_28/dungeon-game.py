class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row = len(dungeon)
        col = len(dungeon[0])

        hp = [[float('inf') for _ in range(col + 1)] for _ in range(row + 1)]
        hp[row][col - 1] = 1
        hp[row - 1][col] = 1
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                need = min(hp[i + 1][j], hp[i][j + 1]) - dungeon[i][j]
                hp[i][j] = 1 if need <= 0 else need
        return hp[0][0]


# 核心思想: 填充法
# [
#     [-2,-3,3],
#     [-5,-10,1],
#     [10,30,-5]
# ]
#
# [
#     [inf, inf, inf, inf],
#     [inf, inf, inf, inf],
#     [inf, inf, 6, 1],
#     [inf, inf, 1, inf]
# ]
# [
#     [inf, inf, inf, inf],
#     [inf, inf, inf, inf],
#     [inf, 1, 6, 1],
#     [inf, inf, 1, inf]
# ]
#
# [
#     [inf, inf, inf, inf],
#     [inf, inf, inf, inf],
#     [1, 1, 6, 1],
#     [inf, inf, 1, inf]
# ]
#
# [
#     [inf, inf, inf, inf],
#     [inf, inf, 5, inf],
#     [1, 1, 6, 1],
#     [inf, inf, 1, inf]
# ]
#
# [
#     [inf, inf, inf, inf],
#     [inf, 11, 5, inf],
#     [1, 1, 6, 1],
#     [inf, inf, 1, inf]
# ]
#
# [
#     [inf, inf, inf, inf],
#     [6, 11, 5, inf],
#     [1, 1, 6, 1],
#     [inf, inf, 1, inf]
# ]
#
# [
#     [inf, inf, 2, inf],
#     [6, 11, 5, inf],
#     [1, 1, 6, 1],
#     [inf, inf, 1, inf]
# ]
#
# [
#     [inf, 5, 2, inf],
#     [6, 11, 5, inf],
#     [1, 1, 6, 1],
#     [inf, inf, 1, inf]
# ]
#
# [
#     [7, 5, 2, inf],
#     [6, 11, 5, inf],
#     [1, 1, 6, 1],
#     [inf, inf, 1, inf]
# ]

