class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.data[key]
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if l == 0: return ""
        return arr[l - 1][0]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)