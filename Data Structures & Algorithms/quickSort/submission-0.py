# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def qs(arr, s, e):
            if e - s + 1 <= 1:
                return pairs
            pivot = arr[e].key
            left = s
            for i in range(s, e):
                if arr[i].key < pivot:
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1
            
            arr[left], arr[e] = arr[e], arr[left]

            qs(arr, s, left - 1)
            qs(arr, left + 1, e)

            return pairs
        return qs(pairs, 0, len(pairs) - 1)