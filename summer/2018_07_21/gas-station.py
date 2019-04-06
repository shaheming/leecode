class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = [g - c for g, c in zip(gas, cost)]
        if sum(diff)<0:
            return -1
        tank = 0
        length = len(gas)
        for index in range(length):
            tmp_index = index

            while True:
                tank += gas[tmp_index]
                tank -= cost[tmp_index]
                if tank < 0:
                    break
                tmp_index = (tmp_index + 1) % length
                # print(tmp_index,index)
                if tmp_index == index:
                    return index
            tank = 0

        return -1
#这个问题的等价问题是最大子序列和问题
#其最精妙的证明过程是以负数开头，或者是以负子序列开头的序列不是最大子序列
#对于这个题而言，以 gas[i] - cost[i] < 0 or sum(gas[j] - cost[j]) < 0 (j=0,1,2,3,4) 的加油站都是不可到达的
#和大于零的序列一定有一个
#对于一个循环数组，如果这个数组整体和 SUM >= 0，
# 那么必然可以在数组中找到这么一个元素：从这个数组元素出发，绕数组一圈，能保证累加和一直是出于非负状态。
# 只是那个为非负的数作为起点就可以

    def canCompleteCircuit2(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = [g - c for g, c in zip(gas, cost)]
        if sum(diff)<0:
            return -1
        tank = 0
        length = len(gas)
        for index in range(length):
            tmp_index = index

            while True:
                tank += gas[tmp_index]
                tank -= cost[tmp_index]
                if tank < 0:
                    break
                tmp_index = (tmp_index + 1) % length
                # print(tmp_index,index)
                if tmp_index == index:
                    return index
            tank = 0

        return -1


s = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print(s.canCompleteCircuit2(gas, cost))
