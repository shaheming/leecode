class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 0:return 0
        num = [1 for i in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                num[i] = num[i-1]+1
        print(num)
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1] > ratings[i]:
                num[i-1] = max(num[i]+1,num[i-1])
        return sum(num)

#这道题和灌水那道题一样,但是这一次可以之比较
#用从左往右和从从右往左的方法两次遍历的方法确定趋势