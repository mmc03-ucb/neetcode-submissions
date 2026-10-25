class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        if last digit is not 9,
        just increase last digit by +1
        if last digit is 9,
        change number to 0 and use carry,
        iteratively continue to left and same until carry 0
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i]
            num += carry
            carry = num // 10
            num = num % 10
            digits[i] = num
            if not carry:
                return digits
        
        if carry:
            return [carry] + digits
