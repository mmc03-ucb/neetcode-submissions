class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Initialize an array of len 26 with 0s where index represents letter disp from ord("a") and val represents count of letter
        Loop through string to count letters and increment array index
        compare arrays for s and t
        runtime: len(max(s), max(t))
        space: O(1)
        """
        count_s = [0] * 26
        count_t = [0] * 26

        for c in s:
            index = ord(c) - ord("a")
            count_s[index] += 1
        
        for c in t:
            index = ord(c) - ord("a")
            count_t[index] += 1
        
        return count_s == count_t

