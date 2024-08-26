class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split('/')
        print(dirs)
        for dir in dirs:
            if dir == \.\ or dir == \\:
                continue
            elif dir == \..\:
                if stack:
                    stack.pop()
            else:
                stack.append(dir)

        final_path = \/\ + \/\.join(stack)
        return final_path