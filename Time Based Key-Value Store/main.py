class TimeMap():

    def __init__(self):
        self.store = {}  # key : [[value, timestamp]]

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):

        values = self.store.get(key, [])
        res = ""
        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            # prawidłowy timestamp
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

timeMap = TimeMap();
timeMap.set("foo", "bar", 1);
timeMap.get("foo", 1);
timeMap.get("foo", 3);
timeMap.set("foo", "bar2", 4);
timeMap.get("foo", 4);
timeMap.get("foo", 5);