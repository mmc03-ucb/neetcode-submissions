# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return pairs
        state = [pairs.copy()]

        for i in range(1, len(pairs)):

            j = i - 1

            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                temp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = temp
                j -= 1

            state.append(pairs.copy())
        
        return state