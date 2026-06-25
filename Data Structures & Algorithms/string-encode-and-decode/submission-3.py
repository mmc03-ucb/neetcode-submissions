class Solution:
    # encode with len(str) + "#"
    # decode with pointers i,j. when i reaches a #. len of str is s[j:i]. then decoded str is s[i+1: len]. Then move i,j to i+len

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

        # "4#neet4#code4#love3#you"

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        j = i
        while i < len(s):
            if s[i] == "#":
                len_str = int(s[j:i]) # 4
                decoded_s = s[i+1: i + 1 + len_str] # [2:6]
                print(decoded_s)
                decoded_str.append(decoded_s)
                i += len_str + 1 
                j = i
            i += 1
        
        return decoded_str