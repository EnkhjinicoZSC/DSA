class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        _s1, _s2 = len(s1), len(s2)
        s1_freq = Counter(s1)
        l = 0
        window = Counter(s2[:_s1])
        if s1_freq == window:
            return True

        for r in range(_s1, _s2):
            window[s2[r]] += 1
            window[s2[r - _s1]] -= 1
            if not window[s2[r - _s1]]:
                del window[s2[r - _s1]]

            if s1_freq == window:
                return True
        return False

