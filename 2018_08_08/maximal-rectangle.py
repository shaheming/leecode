class Solution:
    def maximalRectangle(self, matrix):
        if len(matrix) == 0: return 0
        row = len(matrix)
        col = len(matrix[0])
        left = [0 for _ in range(col)]
        right = [col for _ in range(col)]
        height = [0 for _ in range(col)]
        maxA = 0
        for r in range(row):
            cur_left = 0
            cur_right = col
            for c in range(col):
                if matrix[r][c] == "1":
                    height[c] += 1
                else:
                    height[c] = 0

            for c in range(col - 1, -1, -1):
                if matrix[r][c] == "1":
                    right[c] = min(right[c], cur_right)
                else:
                    right[c] = col
                    cur_right = c

            for c in range(col):
                if matrix[r][c] == '1':
                    left[c] = max(left[c], cur_left)
                else:
                    left[c] = 0
                    cur_left = c + 1

            for l, r, h in zip(left, right, height):
                maxA = max(maxA, (r - l) * h)

        return maxA

    def maximalRectangle1(self, matrix):
        if not matrix or not matrix[0]: return 0
        col = len(matrix[0])
        height = [0] * (col + 1)
        ans = 0
        for row in matrix:
            for c in range(col):
                height[c] = height[c] + 1 if row[c] == '1' else 0
            stack = [-1]
            for i in range(col + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans

    def maximalRectangle1(self, matrix):
        if not matrix or not matrix[0]: return 0  # Use this method the check matrix
        col = len(matrix[0])
        height = [0 for _ in range(col + 1)]
        ans = 0
        for row in matrix:
            for c in range(col):
                if row[c] == '1':
                    height[c] += 1
                else:
                    row[c] = 0
            stack = [-1]
            for i in range(col + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                stack.append(i)



s = Solution()
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
# a = s.maximalRectangle(matrix)
# print(a)

#这里的核心思想是找 histogram 里面的最大长方形的思想
stack = [-1]
height = [1, 2, 3, 4, 4, 4, 4, 5, 0, 0, 1, 1, 0]
ans = 0
for i in range(len(height)):
    while height[i] < height[stack[-1]]:
        print(stack, height[stack[-1]])
        h = height[stack.pop()]
        w = i - 1 - stack[-1]
        ans = max(ans, h * w)
    stack.append(i)
