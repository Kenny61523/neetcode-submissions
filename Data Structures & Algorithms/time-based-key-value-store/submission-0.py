class TimeMap:

    def __init__(self):
        self.store = {}# store is the vairable name for the class

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # self.store[key] = self.stroe.get(key, []) # if key has no values than set to empty list
        values = self.store.get(key, []) # if key has no values than set to empty list

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res 
        






