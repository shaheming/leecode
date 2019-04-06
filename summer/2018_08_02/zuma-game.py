class Solution:
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        h = {}
        for i in hand:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        return self.dfs(board,h)

    def dfs(self, board, hand):
        if len(board) == 0: return 0
        ans = float('inf')
        i, j = 0, 0
        while i < len(board):
            while j < len(board) and board[i] == board[j]: j += 1
            color = board[i]
            b = 3 - (j - i)
            if hand.get(color,0) >= b:
                nb = self.shrink(board[0:i] + board[j:])
                hand[color] -= b
                r = self.dfs(nb, hand)
                if r >= 0: ans = min(ans, r + b)
                hand[color] += b
            i=j
        return -1 if ans == float("inf") else ans

    def shrink(self, board):
        index = 0
        while index < len(board):
            head = board[index]
            i = index
            counter = 0
            while i < len(board) and head == board[i]:
                counter += 1
                i += 1
            if counter > 2:
                board = board[:index] + board[i:]
                index = 0
            else:
                index = i

        return board


board = "RBYYYBBRRB"
s = Solution()
s.shrink(board)
print(s.findMinStep("WRRBBW","RB"))
