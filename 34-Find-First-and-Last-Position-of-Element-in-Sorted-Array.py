class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.binSearch(nums, target, True), self.binSearch(nums, target, False)
        return [left, right]


    
    def binSearch(self, nums, target, isLeft):
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                idx = mid
                if isLeft:
                    r = mid - 1
                else:
                    l = mid + 1
        return idx


                