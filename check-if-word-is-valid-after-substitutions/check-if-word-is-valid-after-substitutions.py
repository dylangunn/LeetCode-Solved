class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char != 'c':
                stack.append(char)
            else:
                if stack[-2:] != ['a','b']:
                    return False
                stack.pop()
                stack.pop()
        return not stack