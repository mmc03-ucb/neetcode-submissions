class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        res = nums[0]

        for num in nums[1:]:
            if num < 0:
                maxProd, minProd = minProd, maxProd
            
            maxProd = max(num, maxProd * num)
            minProd = min(num, minProd * num)

            res = max(maxProd, res)
        
        return res