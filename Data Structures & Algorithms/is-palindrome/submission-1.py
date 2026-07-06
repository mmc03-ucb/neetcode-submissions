class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        2 pointers moving from each end
        if alphanumeric, convert to lower and compare
        if not same, return False
        if same, increment from left and decrement from right
        if not alphanumeric or space, increment/decrement until valid
        if l == r:
            return True
        TC: O(n) where n is length of string
        SC: O(1)
        """
        l, r = 0, len(s) - 1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            
            if l < r:
                if s[l].lower() != s[r].lower():
                    return False
            l += 1
            r -= 1
        return True