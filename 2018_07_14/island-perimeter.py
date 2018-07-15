# https://leetcode.com/problems/island-perimeter/description/
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.row_size = len(grid)
        if self.row_size == 0:
            return 0
        self.col_size = len(grid[0])
        count = 0
        for r in range(self.row_size):
            for c in range(self.col_size):
                if grid[r][c]==1:
                    count += self.get_perimeter(grid, r, c)
        return count

    def get_perimeter(self, grid, row, col):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0
        for r, c in directions:
            if not (row + r >= self.row_size or row + r < 0 or col + c < 0 or col + c >= self.col_size) \
                    and grid[row + r][col + c] == 1:
                pass
            else:
                count += 1

        return count

grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

s = Solution()
r=s.islandPerimeter(grid)
print(r)