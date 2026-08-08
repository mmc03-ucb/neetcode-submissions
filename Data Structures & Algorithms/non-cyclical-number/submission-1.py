class Solution:
    def isHappy(self, n: int) -> bool:
        numSet = set()

        curr = n

        while curr not in numSet:
            numSet.add(curr)
            currString = str(curr)
            total = 0
            for d in currString:
                int_d = int(d)
                total += (int_d ** 2)
            curr = total
            if curr == 1:
                return True
        
        return False