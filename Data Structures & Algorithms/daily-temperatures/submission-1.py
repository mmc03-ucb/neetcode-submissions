class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            curr = temperatures[i]
            
            while len(stack) > 0 and curr > stack[-1][0]:
                days = i - stack[-1][1]
                ix = stack[-1][1]
                output[ix] = days
                stack.pop()
            
            stack.append((curr, i))

        return output
            
