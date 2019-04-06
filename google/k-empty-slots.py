class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if len(flowers) == 0:
            return -1
        dayM = float('inf')
        visted = set()
        for i in range(len(flowers)):
            # if flowers[i] - k - 1 <= 0
            # end = flowers[i] + k + 1
            # else start = flowers[i] - k - 1
            # end = flowers[i] + k + 1
            visted.add(flowers[i])
            start = flowers[i] - k - 1
            end = flowers[i] + k + 1
            for v in range(flowers[i] - 1, start - 1, -1):
                if v in visted:
                    start -= 1

            for v in range(flowers[i] + 1, end + 1):
                if v in visted:
                    end += 1
            for j in en
            for j in range(i+1, len(flowers)):
                if flowers[j] == start or flowers[j] == end:
                    print(flowers[i], flowers[j], start, end, j+1, dayM,j)
                    #(70, 64, 64, 75, 14, 17, 13)
                    dayM = min(dayM, j + 1)
                    break
                if flowers[j] < flowers[i] and flowers[j] > start:
                    start -= 1
                if flowers[j] > flowers[i] and flowers[j] < end:
                    end += 1
                if start <= 0 and end >= len(flowers):
                    break

        if dayM < float('inf'):
            return dayM
        return -1


f = [5,39,25,28,16,58,70,29,67,24,78,13,9,64,98,38,44,96,27,88,75,84,69,34,55,12,47,33,77,15,31,74,2,26,76,10,17,72,100,36,6,90,4,95,49,21,94,79,62,32,1,35,60,18,3,53,82,48,54,30,19,87,40,85,68,57,11,42,92,61,71,37,14,51,50,83,22,93,91,65,99,52,7,46,89,80,20,8,97,86,23,66,81,59,56,63,43,41,73,45]

k = 4


s = Solution()
r = s.kEmptySlots(f, k)
print(r)

def find(active, flower):
        left, right = 0, len(active) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if active[left] <= flower:
                left = mid
            else:
                right = mid
        if active[right] <= flower:
            return right
        else:
            return left
