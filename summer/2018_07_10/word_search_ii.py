#https://leetcode.com/problems/word-search-ii/submissions/1
#思路,构造要搜索的词的树，对树进行遍历
class Solution:
    def __init__(self):
        self.res = set()
        self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # make trie
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            # add end
            t['#'] = '#'
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(board, row, col, trie, '')
        return list(self.res)
        # return result

    def dfs(self, board, row, col, trie, pre):
        if '#' in trie:
            self.res.add(pre)
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == "*":
            return
        if board[row][col] != "*" and board[row][col] in trie:
            temp = board[row][col]
            board[row][col] = "*"
            for r, c in self.directions:
                self.dfs(board, row + r, col + c, trie[temp], pre + temp)
            board[row][col] = temp


board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]

words = ["oath", "pea", "eat", "rain"]

s = Solution()
print(s.findWords(board, words))
# tree = WordTree(board, words)
