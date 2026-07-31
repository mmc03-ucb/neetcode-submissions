class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        sliding window
        when we come across a 1, we set left pointer there
        and move right pointer until we come across a 0
        while incrementing 1s counter
        we update the max counter based on the current count
        """
        maxOnes = 0
        count = 0

        for num in nums:
            if num == 0:
                count = 0
            else:
                count += num
                maxOnes = max(count, maxOnes)
        
        return maxOnes

        # TC: O(n)
        # SC: O(1)