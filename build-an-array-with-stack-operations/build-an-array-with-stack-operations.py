class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if not target: return []
        prev = 0
        ret = []
        for num in target:
            numTimes = num - prev - 1
            for time in range(numTimes):
                ret.extend(["Push","Pop"])
            ret.append("Push")
            prev = num
        return ret