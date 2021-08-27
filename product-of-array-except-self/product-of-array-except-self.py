class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums) - 1
        lower = nums[:]
        upper = nums[:]
        for i in range(length):
            up = length - 1 - i
            lower[i+1] *= lower[i]
            upper[up] *= upper[up + 1]
        res = [upper[1]]
        for i in range(1,length):
            res.append(lower[i-1] * upper[i+1])
        res.append(lower[length-1])
        return res