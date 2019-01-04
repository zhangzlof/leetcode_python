# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        res = []
        intervals.sort(key=lambda x: x.start)
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(intervals[i].end,res[-1].end)
                res[-1].start = min(res[-1].start,intervals[i].start)
            else:
                res.append(intervals[i])
        return res
