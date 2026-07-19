class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def compare(s_count, t_count):
            for letter, count in t_count.items():
                if s_count[letter] < count:
                    return False
            return True

        if len(s) == len(t):
            if Counter(s) == Counter(t):
                return s
            else:
                return ""
        elif len(s) < len(t):
            return ""
        else:
            print("enter else")
            t_count = Counter(t)
            l = 0
            s_count = Counter()
            length = float("INF")
            shortest = ""
            for r in range(len(s)):
                s_count[s[r]] += 1
                while s[r] in t_count and (r - l + 1) >= len(t) and compare(s_count, t_count):
                    if (r - l + 1) < length:
                        length = r - l + 1
                        shortest = s[l: r + 1]
                    s_count[s[l]] -= 1
                    if s_count[s[l]] == 0:
                        del s_count[s[l]]
                    l += 1

            return shortest

