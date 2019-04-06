# 如果能够装水有三种情况 1.
# >>> [1,2][-1]
# 2
# >>> [1,2][0:-1]
# [1]
# 思路一: 从自己望过去找出周围最高的作为最高点(一种搜索)。
# 思路二: 一个一个
class Solution:
    def trap(self, height):
        """
         :type height: List[int]
         :rtype: int
         """
        counter = 0
        length = len(height)
        for i in range(1, length - 1):
            j = i
            max_left = max_right = 0
            while j >= 0:
                max_left = max(max_left, height[j])
                j -= 1
            j = i
            while j < length:
                max_right = max(max_right, height[j])
                j += 1
            counter += min(max_left, max_right) - height[i]

            i += 1
        return counter

    def trap2(self, height):
        """
         :type height: List[int]
         :rtype: int
         """
        counter = 0
        length = len(height)
        max_left = [0] * length
        max_right = [0] * length
        max_left[0] = height[0]
        for i in range(1, length):
            max_left[i] = max(max_left[i - 1], height[i])
        max_right[- 1] = height[- 1]
        for i in range(length - 2, 0, -1):
            max_right[i] = max(max_right[i + 1], height[i])
        for i in range(1, length - 1):
            counter += min(max_left[i], max_right[i]) - height[i]
        return counter


height = [5, 2, 1, 2, 1, 5]
s = Solution()
print(s.trap(height))
print(s.trap2(height))
