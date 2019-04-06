import collections
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if wordDict == []:
            return False
        maxLength = max([len(w) for w in wordDict])
        queue = collections.deque([])
        if s in wordDict:
            return True        
        for i in range(min(maxLength,len(s))-1, -1,-1):
            if s[:i+1] in wordDict:
                queue.append(s[i+1:])
        while len(queue) > 0:
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if tmp in wordDict:
                    return True
                for i in range(min(maxLength,len(tmp))-1,-1,-1):
                    if tmp[:i+1] in wordDict:
                        queue.append(tmp[i+1:])
        
        return False

s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(Solution().wordBreak(s,wordDict))