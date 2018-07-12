# https://leetcode.com/problems/word-ladder/discuss/40729/Compact-Python-solution
#思路，用一个队列来实现广度优先搜索
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = [[beginWord, 1]]
        while len(queue) > 0:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0


#
# beginWord = "lost"
# endWord = "miss"

# wordList = ["most", "mist", "miss", "lost", "fist", "fish"]
beginWord = "hit"
endWord = "dog"
wordList = ["hot", "dog", "dot"]
s = Solution()
print(s.ladderLength(beginWord, endWord, wordList))
# print(s.isValid('leet', 'lode'))
