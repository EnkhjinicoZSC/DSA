class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2],    0
        #  l     m     r
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        partition_idx = l
        
        # 2 parts
        # 1: from 0th to partition
        # 2: from partition to end
        l, r = 0, len(nums) - 1
        if target <= nums[r]:
            i, j = partition_idx, r
        else:
            i, j = 0, partition_idx - 1

        print(i, j)
        
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1