class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts, ends = [], []
        for f in flowers:
            starts.append(f[0])
            ends.append(f[1] + 1)
        starts.sort()
        ends.sort()
        res = []
        for p in people:
            i = bisect_right(starts, p)
            j = bisect_right(ends, p)
            res.append(i-j)
        return res


