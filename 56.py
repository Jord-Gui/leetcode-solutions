# Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        ret_val = []
        intervals.sort(key=lambda x: x[0])
        while len(intervals) > 0:
            current_interval = intervals.pop(0)
            i = 0
            while i < len(intervals):
                next_interval = intervals[i]
                if next_interval[0] <= current_interval[1]:
                    next_interval = intervals.pop(i)
                    if current_interval[1] < next_interval[1]:
                        current_interval = [current_interval[0], next_interval[1]]
                    else:
                        current_interval = [current_interval[0], current_interval[1]]
                else:
                    i += 1
            ret_val.append(current_interval)
        return ret_val
