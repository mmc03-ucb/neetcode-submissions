class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window that expands until a repeating character is reached. if repeating character, window is shortened. 
        # track longest window using set to easily check for duplicates
        
        substring = set()
        longest = 0

        win_start = 0
        length = 0
        for win_end in range(len(s)):
            char = s[win_end]
            # if duplicate, shorten window and remove duplicate
            while char in substring:
                substring.remove(s[win_start])
                win_start += 1
                length -= 1
            substring.add(char)
            length += 1
            longest = max(length, longest)
        return longest

