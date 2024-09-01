class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        stack = []
        for num2 in nums2:
            while stack and num2 > stack[-1]:
                h[stack.pop()] = num2
            stack.append(num2)
        while stack:
            h[stack.pop()] = -1
        return [h.get(num, -1) for num in nums1]
