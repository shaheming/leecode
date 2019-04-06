import collections


class Solution:
    def keyboard(self, s, keyboard):
        if len(s) == 0:
            return 0
        row, col = 0, 0
        for r in range(len(keyboard)):
            for c in range(len(keyboard[0])):
                if int(s[0]) == keyboard[r][c]:
                    row = r
                    col = c
        count = 0
        for i in range(len(s)):
            distance, row, col = self.move(row, col, s[i], keyboard)
            count += distance
        return count

    def move(self, row, col, nextStr, keyboard):
        if int(nextStr) == keyboard[row][col]:
            return 0, row, col

        queue = collections.deque([(row, col)])
        visited = set()
        distance = 0
        while len(queue) != 0:
            distance += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                visited.add(keyboard[row][col])
                for r, c in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                    if self.isInBound(row+r, col+c, keyboard):
                        if keyboard[row+r][col+c] == int(nextStr):
                            return distance, row+r, col+c
                        else:
                            if keyboard[row+r][col+c] not in visited:
                                queue.append((row+r, col+c))
            

    def isInBound(self, row, col, keyboard):
        if row < 0 or col < 0 or row >= len(keyboard) or col >= len(keyboard[0]):
            return False
        else:
            return True


keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
string = "23654789"
s = Solution()
print(s.keyboard(string, keyboard))
