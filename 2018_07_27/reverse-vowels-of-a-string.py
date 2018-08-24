class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(list("aeiouAEIOU"))
        # s = list(s)
        # stack = []
        # for i in range(len(s)):
        #     if s[i] in vowels:
        #         stack.append(s[i])
        #         s[i]="##"
        # for i in range(len(s)):
        #     if s[i] == "##":
        #         s[i] = stack.pop()
        # return "".join(s)
        s = list(s)
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] in vowels and s[end] in vowels:
                s[start],s[end] = s[end],s[start]
                start+=1
                end-=1
            if  start < len(s) and s[start] not in vowels:
                start+=1
            if end >=0 and s[end] not in vowels:
                end-=1
        return "".join(s)

