class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            else:
                curr = num
                curr_len = 0
                while curr in numSet:
                    curr += 1
                    curr_len += 1
                length = max(length, curr_len)
        
        return length