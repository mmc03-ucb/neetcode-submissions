class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charCount = defaultdict(int)

        longest = 0
        l, r = 0, 0

        while r < len(s):
            charCount[s[r]] += 1

            while charCount[s[r]] > 1:
                charCount[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest