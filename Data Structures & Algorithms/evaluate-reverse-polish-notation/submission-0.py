class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()

        for token in tokens:
            if token.isnumeric() or (token[0] == "-" and token[1:].isnumeric()):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                match token:
                    case "+":
                        result = num1 + num2
                    case "-":
                        result = num1 - num2
                    case "*":
                        result = num1 * num2
                    case "/":
                        result = num1 / num2
                        result = int(result)
                stack.append(result)
        return stack[-1] 