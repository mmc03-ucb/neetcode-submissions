class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # use set to check len of set(nums). If there are no repeats, len of set will be equal to original length
         
         return len(set(nums)) != len(nums)

         #O(1) runtime for len.