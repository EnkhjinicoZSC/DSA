class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        for ch in text:
            if ch in "balloon":
                counter[ch] += 1
        if any(c not in counter for c in "balloon"):
            return 0
        else:
            return min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"])
