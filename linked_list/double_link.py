class Solution:
    def count(self, n, commands):
        self.left = [0]+[i for i in range(n+1)]
        self.right = [i for i in range(1, n+2)]
        self.reverse = False
        for command in commands:
            if command[0] == 1:
                x = command[1]
                y = command[2]
                if self.left[y] == x and self.right[x] == y:
                    pass
                else:
                    xLeft = self.left[x]
                    xRight = self.right[x]
                    yLeftLeft = self.left[self.left[y]]
                    yLeft = self.left[y]

                    self.left[x] = yLeftLeft
                    self.right[x] = y
                    self.right[yLeftLeft] = x
                    self.left[y] = x

                    self.right[xLeft] = yLeft
                    self.left[yLeft] = xLeft
                    self.right[yLeft] = xRight
                    self.left[xRight] = yLeft
        
        print(self.left)
        print(self.right)


        start = 0
        r = [self.right[0]]
        while start != n:
            start = self.right[start]
            r.append(start)
        print(r)

    def link(self, l, r):
        self.left[l] = r
        self.right[r] = l


s = Solution()
s.count(6, [[1, 4, 1]])
