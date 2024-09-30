class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def rec(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                rec(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                rec(openN, closedN + 1)
                stack.pop()

        rec(0, 0)
        return res
            