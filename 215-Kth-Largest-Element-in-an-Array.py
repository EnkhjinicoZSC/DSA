class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in range(k):
            minheap.append(nums[i])
        heapq.heapify(minheap)
        print(minheap)
        for i in range(k, len(nums)):
            if nums[i] > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, nums[i])
        return minheap[0]