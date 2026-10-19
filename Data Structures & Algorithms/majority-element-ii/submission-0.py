class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        output = []

        for num, c in count.items():
            if c > (len(nums) / 3):
                output.append(num)

        return output
            