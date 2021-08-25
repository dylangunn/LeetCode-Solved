class Solution:
    def minFlips(self, target: str) -> int:
        cur = target[0]
        ans = 1
        end = len(target)
        for i in range(1,end):
            tmp = target[i]
            if tmp != cur:
                cur = tmp
                ans += 1
        if target[0] == '0':
            ans -= 1
        return ans
                