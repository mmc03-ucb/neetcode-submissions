class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_Count = Counter(s1)

        s2_Count = defaultdict(int)

        l = 0

        for r in range(len(s2)):
            s2_Count[s2[r]] += 1
            if (r - l + 1) > len(s1):
                s2_Count[s2[l]] -= 1
                if s2_Count[s2[l]] == 0:
                    del s2_Count[s2[l]]
                l += 1
            
            if s1_Count == s2_Count:
                return True
        
        return False
