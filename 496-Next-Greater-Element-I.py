class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        h = defaultdict(list)
        for idx, num in enumerate(nums2):
            h[num].append(idx)
        print(h)
        for i, num in enumerate(nums1):
            if num in h:
                idx = h[num][0]
                for j in range(idx, len(nums2)):
                    if nums2[j] > num:
                        ans[i] = nums2[j]
                        break
        return ans