class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}

        stack = []

        for b in s:
            if b in brackets:
                if len(stack) == 0:
                    return False
                elif stack[-1] != brackets[b]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(b)
        
        return True if len(stack) == 0 else False