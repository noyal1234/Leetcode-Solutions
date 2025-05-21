class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for i in s:
            if i in d:
                if stack and d[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
                
