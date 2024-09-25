class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(cost) > sum(gas):
            return -1 
        curr = 0
        idx = 0
        for i in range(n):
            curr += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                idx = i + 1
        return idx
