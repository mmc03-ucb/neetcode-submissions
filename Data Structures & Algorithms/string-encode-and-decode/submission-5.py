"""
Encode string in format len(s) + # + s
Decode: while r not end of s
            increment l until # to find len(s)
            convert len to int
            increment l by 1 to beginning of string
            set r to l + len
            add s[l:r] to list
            set l to r
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encode string in format len(s) + # + s
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        l,r = 0, 0
        output = []
        while r < len(s):
            curr_len = ""
            # increment l until # to find len(s)
            while s[l] != "#":
                curr_len += s[l]
                l += 1
            # convert len to int
            curr_len = int(curr_len)
            # increment l by 1 to beginning of string
            l += 1
            # set r to l + len
            r = l + curr_len
            # add s[l:r] to list
            output.append(s[l:r])
            #set l to r
            l = r
        
        return output
            
