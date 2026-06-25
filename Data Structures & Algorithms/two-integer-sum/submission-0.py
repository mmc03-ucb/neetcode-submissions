class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Initialize dictionary where key is num and value is index
        Loop through nums and store key is num and value is index
        Loop through nums again and find diff (target - num)
            Check if diff in dictionary and dictionary[diff] != current index
                True: return [currIndex, diffIndex]
                False: continue
        TC: O(n)
        SC: O(n)
        """

        numIndices = {}
        for i in range(len(nums)):
            numIndices[nums[i]] = i
        
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in numIndices and i != numIndices[diff]:
                return [i, numIndices[diff]]
        
        return [-1,-1]
