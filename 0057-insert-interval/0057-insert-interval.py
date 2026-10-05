class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        for start,end in intervals[0:]:
            if start<=result[-1][1]:
                result[-1][1]=max(result[-1][1],end)
            else:
                result.append([start,end])
        return result