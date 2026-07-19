class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_frequent_letter = ""
        highest = 0
        letter_count = defaultdict(int)

        l = 0
        length = 0

        for r in range(len(s)):
            letter_count[s[r]] += 1
            if letter_count[s[r]] > highest:
                highest = letter_count[s[r]]
                most_fequent_letter = s[r]
            while (r - l + 1) - highest > k:
                letter_count[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        
        return length