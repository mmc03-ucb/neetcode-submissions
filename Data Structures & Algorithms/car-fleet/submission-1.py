class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        combined = []

        for p, s in zip(position, speed):
            combined.append([p, s])
        
        combined.sort(reverse = True)

        for p, s in combined:
            t = (target - p) / s
            stack.append(t)
            
            while len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
