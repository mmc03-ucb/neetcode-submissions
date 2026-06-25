class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = collections.deque()
        stack.append(0)

        for day in range(1, len(temperatures)):
            temp = temperatures[day]
            while stack and temp > temperatures[stack[-1]]:
                answer[stack[-1]] = day - stack[-1]
                stack.pop()
            stack.append(day)
        
        return answer