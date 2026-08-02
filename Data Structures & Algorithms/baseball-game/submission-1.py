class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op[0] == "-" or op.isnumeric():
                stack.append(int(op))
            elif op == "+":
                s2 = stack[-1]
                s1 = stack[-2]
                new = s1 + s2
                stack.append(new)
            elif op == "D":
                new = stack[-1] * 2
                stack.append(new)
            else:
                stack.pop()
        
        return sum(stack)