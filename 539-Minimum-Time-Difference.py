class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for idx, time in enumerate(timePoints):
            hours, mins = time.split(\:\)
            timePoints[idx] = int(hours) * 60 + int(mins)

        timePoints.sort()
        res = timePoints[0] + 1440 - timePoints[-1]
        for i in range(1, len(timePoints)):
            diff = timePoints[i] - timePoints[i-1]
            res = min(res, diff)

        return res

