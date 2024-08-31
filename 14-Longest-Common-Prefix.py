class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = \\
        for each in zip(*strs):
            if len(set(each)) == 1:
                res += each[0]
            else:
                return res
        return res