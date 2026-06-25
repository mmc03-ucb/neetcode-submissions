from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        brackets_dictionary = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in brackets_dictionary:
                if not stack:
                    return False
                opening_bracket = stack.pop()
                if brackets_dictionary[c] != opening_bracket:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0