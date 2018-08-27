class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = x ^ y
        div = 2 ** 30
        counter = 0
        while div >= 1:
            if r >= div:
                counter += 1
                r = r % div
            div /= 2

        return counter
