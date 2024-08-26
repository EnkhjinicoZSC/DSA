class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        \\\
        Do not return anything, modify nums1 in-place instead.
        \\\
        last1, last2 = m - 1, n - 1
        for idx in range(n + m - 1, -1, -1):
            if last2 < 0:
                break
            if last1 >= 0 and nums1[last1] > nums2[last2]:
                nums1[idx] = nums1[last1]
                last1 -= 1
            else:
                nums1[idx] = nums2[last2]
                last2 -= 1

