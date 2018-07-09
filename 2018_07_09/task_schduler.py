# meduim
# https://leetcode.com/problems/task-scheduler/description/
# 贪婪算法
# Task Scheduler 贪婪算法
# 我们可以将n+1个时间片作为一个分组。这个分组中要填充各不相同的任务或空闲。
# 可以把一次调度看成是一个长度为n+1的环。cycle = n + 1. 如果这cycle个坑，必须由不同的task来填。如果没有这么多种类的 task，那么剩下的坑cpu就只能空转
# 那么填坑的时候使用哪些 task 呢。
# 我们尽可能的使用剩余的 task 中频数最高的 task,
# 因为每个 cycle 中不能重复，如果不优先安排掉 频数最高的 task
# 就要用idle来隔开他们。

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_dict = {}
        for task in tasks:
            if task_dict.get(task, None) is None:
                task_dict[task] = 1
            else:
                task_dict[task] += 1
        sorted_task = sorted(task_dict.items(), key=lambda k: -k[1])
        counter = 0
        while len(sorted_task) > 0:
            for i in range(n + 1):
                try:
                    task = sorted_task[i][0]
                    counter += 1
                    task_dict[task] -= 1
                    if task_dict[task] == 0:
                        del task_dict[task]
                except:
                    if len(task_dict.items()) != 0:
                        counter += n + 1 - i
                    break
            sorted_task = sorted(task_dict.items(), key=lambda k: -k[1])
        return counter


s = Solution()
out = s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
print(out)
