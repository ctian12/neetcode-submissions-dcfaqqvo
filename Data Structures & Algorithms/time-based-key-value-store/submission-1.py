class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        data = self.d[key]
        l, r = 0, len(data) - 1
        out = ""

        while l <= r:
            m = (l + r) // 2
            if data[m][0] <= timestamp:
                out = data[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return out
        
