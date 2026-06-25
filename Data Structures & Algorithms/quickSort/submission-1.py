# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def qs(s, e):
            if e - s + 1 <= 1:
                return pairs
            pivot = pairs[e].key
            left = s
            for i in range(s, e):
                if pairs[i].key < pivot:
                    pairs[left], pairs[i] = pairs[i], pairs[left]
                    left += 1
            
            pairs[left], pairs[e] = pairs[e], pairs[left]

            qs(s, left - 1)
            qs(left + 1, e)
            return pairs
        return qs(0, len(pairs) - 1)