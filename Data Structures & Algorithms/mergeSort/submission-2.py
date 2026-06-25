# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(arr, s , m, e):
            arrL = arr[s:m+1]
            arrR = arr[m+1:e+1]
            i, j, k = 0, 0, s

            while i < len(arrL) and j < len(arrR):
                if arrL[i].key <= arrR[j].key:
                    arr[k] = arrL[i]
                    i += 1
                else:
                    arr[k] = arrR[j]
                    j += 1
                k += 1
            
            while i < len(arrL):
                arr[k] = arrL[i]
                i += 1
                k += 1
            

            while j < len(arrR):
                arr[k] = arrR[j]
                j += 1
                k += 1
        
        def ms(arr, s, e):
            if e - s + 1 <= 1:
                return arr
            
            m = (s+e) // 2

            ms(arr, s, m)
            ms(arr, m+1, e)

            merge(arr, s, m, e)

            return arr
        
        return ms(pairs, 0, len(pairs) - 1)
