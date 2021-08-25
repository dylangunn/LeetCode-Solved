class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 0x1
        for num in nums:
            if num is 0:
                return 0
            if num < 0:
                res ^= 0x1
        if res == 1:
            return 1
        return -1