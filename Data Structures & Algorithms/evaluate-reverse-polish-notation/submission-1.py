class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                op2 = stack.pop()
                op1 = stack.pop()
                result = op1 + op2
                stack.append(result)
            elif t == "-":
                op2 = stack.pop()
                op1 = stack.pop()
                result = op1 - op2
                stack.append(result)
            elif t == "*":
                op2 = stack.pop()
                op1 = stack.pop()
                result = op1 * op2
                stack.append(result)
            elif t == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                result = op1 / op2
                stack.append(int(result))
            else:
                stack.append(int(t))
        
        return stack[-1]