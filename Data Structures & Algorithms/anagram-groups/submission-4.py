class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Initialize a dictionary where key is a set representing the letter count of a string and the value is the string itself
        loop through strs
            initialize key as [0] * 26 representing letter counts
            loop through s in strs
                increment key[ord(c) - ord("a")] += 1
            convert key array to tuple to make it immutable
            dictionary[set(key)].append(s)
        
        return dictionary.values()
        TC: len(strs) * len(max(s))
        SC: len(strs)
        """

        anagrams = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord("a")] += 1
            
            anagrams[tuple(key)].append(s)
        
        return list(anagrams.values())
