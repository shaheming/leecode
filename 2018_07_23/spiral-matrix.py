# 方法一奔方法，边界裁剪，遍历
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(matrix)
        n = len(matrix[0])
        cBound = [0, n]
        rBound = [0, m]
        row = 0
        cow = 0
        result = []
        result.append(matrix[row][cow])
        count = m * n - 1
        index = 0
        while True:
            (r, c) = direction[index]
            while True:
                row += r
                cow += c
                if index == 0 and cow >= cBound[1]:
                    cow -= c
                    rBound[0] += 1
                    break
                if index == 1 and row >= rBound[1]:
                    row -= r
                    cBound[1] -= 1
                    break
                if index == 2 and cow < cBound[0]:
                    cow -= c
                    rBound[1] -= 1
                    break
                if index == 3 and row < rBound[0]:
                    row -= r
                    cBound[0] += 1
                    break
                result.append(matrix[row][cow])
                count -= 1
            index += 1
            index %= 4
            if count == 0:
                break
        return result

    # [] and [3]
    # []
    #
    # [1] and [3]
    # [3]
    # The single star * unpacks the sequence/collection into positional arguments
    # >>> "1234"[::-1]
    # '4321'
    def spiralOrder2(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder2([*zip(*matrix)][::-1])


s = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = []
r = s.spiralOrder(matrix)
print(r)
[[0, '@', 0],
 [0, 0, 1],
 [1, 1, 1],
 [0, 0, 0]]