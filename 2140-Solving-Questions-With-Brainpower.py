class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(questions):
                return 0
            
            j = i + 1 + questions[i][1]
            return max(dp(j) + questions[i][0], dp(i+1))
        return dp(0)