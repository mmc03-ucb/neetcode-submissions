class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        if len(nums) < 3:
            return output

        nums.sort()
        for i,v in enumerate(nums):
            if v > 0:
                break
            
            if i > 0 and v == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = v + nums[l] + nums[r]
                if total == 0:
                    output.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        
        return output