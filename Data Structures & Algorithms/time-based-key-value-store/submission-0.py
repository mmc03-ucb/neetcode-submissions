class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""
        else:
            l, r = 0, len(self.dictionary[key]) - 1
            val = ""
            while l <= r:
                m = (l+r) // 2
                if self.dictionary[key][m][0] <= timestamp:
                    val = self.dictionary[key][m][1]
                    l = m + 1
                else:
                    r = m - 1
            
            return val
