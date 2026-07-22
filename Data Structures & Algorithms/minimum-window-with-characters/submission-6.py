class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        substring_l = -1
        substring_r = -1
        shortest = float("INF")

        l = 0

        s_count = Counter()
        t_count = Counter(t)

        def compare(t, s):
            print(t_count)
            print(s_count)
            for c, n in t_count.items():
                if s_count[c] < n:
                    return False
            
            return True

        for r in range(len(s)):
            s_count[s[r]] += 1

            # while t is a substring of s, decrement length of substring

            # while t is a substring of s
            while compare(t, s):
                # update shortest length
                if (r - l + 1) < shortest:
                    substring_l = l
                    substring_r = r
                    shortest = r - l + 1

                # decrement s[l] from s_count and remove if 0
                s_count[s[l]] -= 1
                if s_count[s[l]] == 0:
                    del s_count[s[l]]
                
                # decrement length of substring
                l += 1
        
        if substring_l != -1:
            return s[substring_l:substring_r + 1]
        else:
            return ""

                
