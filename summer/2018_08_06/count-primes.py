class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        primes = [1] * n

        for i in range(2, n):
            if primes[i] == 1:
                j = 2 * i
                while j < n:
                    primes[j] = 0
                    j += i

        return sum(primes[2:])
#埃拉托斯特尼筛法
#筛法留下的每一个数k，都不可能被小于等于sqrt(k)的任何一个自然数整除，否则该数会在之前筛的过程中被去掉，证毕。