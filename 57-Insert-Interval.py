class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # case 1: add all intervals nonoverlapping on the left side
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # case 2: merge overlapping intervals and add them to res
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        res.append(newInterval)

        # case 3: add all intervals nonoverlapping on the right side
        while i < n:
            res.append(intervals[i])
            i += 1

        return res