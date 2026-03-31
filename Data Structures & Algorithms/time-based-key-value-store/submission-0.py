class TimeMap:

    def __init__(self):
        self.map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map.setdefault(key, []).append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        valuelist = self.map.get(key, "")
        left = 0
        right = len(valuelist) - 1
        res = ""
        while left <= right:
            middle = (left + right) // 2
            if valuelist[middle][1] <= timestamp:
                res = valuelist[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return res
