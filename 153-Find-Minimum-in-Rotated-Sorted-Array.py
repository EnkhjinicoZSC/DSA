class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[low] and nums[mid] < nums[high]:
                if nums[low] > nums[high]:
                    high = mid
            elif nums[mid] > nums[low] and nums[mid] > nums[high]:   
                if nums[low] > nums[high]:
                    low = mid
            else:
                if nums[high] > nums[low]:
                    return nums[low]
                elif nums[high] < nums[low]:
                    return nums[high]
                else:
                    return nums[low]
