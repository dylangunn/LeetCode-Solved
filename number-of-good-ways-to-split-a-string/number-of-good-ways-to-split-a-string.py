class Solution:
    def numSplits(self, s: str) -> int:
        if not s:
            return None
        left = {s[0]:1}
        right = {}
        for i in range(1,len(s)):
            if s[i] in right: right[s[i]] += 1
            else: right[s[i]] = 1
        ret = 0
        for i in range(1,len(s)):
            if len(left) == len(right):
                ret += 1
            if s[i] in left: left[s[i]] += 1
            else: left[s[i]] = 1
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
        return ret