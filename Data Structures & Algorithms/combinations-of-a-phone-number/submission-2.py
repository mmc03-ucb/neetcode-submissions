class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        output = []
        curr = []

        def backtrack(i):
            if len(curr) == len(digits):
                output.append("".join(curr))
                return

            d = digits[i]
            for c in phone[d]:
                curr.append(c)
                backtrack(i+1)
                curr.pop()
        
        backtrack(0)

        return output

