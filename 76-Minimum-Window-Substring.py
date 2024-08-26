class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == \\ or len(s) < len(t): return \\
        t_freq, window = {}, {}

        for ch in t:
            t_freq[ch] = 1 + t_freq.get(ch, 0)

        required = len(t_freq)
        l, have = 0, 0
        res, resLen = [-1, -1], float(\inf\)

        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)
            if ch in t_freq and window[ch] == t_freq[ch]:
                have += 1
            while have == required:
                if (r - l + 1) < resLen:
                    res = [l, r] 
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l:r+1] if resLen != float(\inf\) else \\

