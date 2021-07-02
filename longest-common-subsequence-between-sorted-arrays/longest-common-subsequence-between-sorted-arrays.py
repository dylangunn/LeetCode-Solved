class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        ret = set()
        tmp = set()
        for i in arrays[0]:
            ret.add(i)
        for arr in arrays:
            for elem in arr:
                if elem in ret:
                    tmp.add(elem)
            ret = tmp.copy()
            tmp.clear()
        return sorted(list(ret))