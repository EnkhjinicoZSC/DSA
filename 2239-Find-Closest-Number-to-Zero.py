class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        x = min([abs(i) for i in nums])
        return x if x in nums else -x