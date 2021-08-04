class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {}
        res = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        for key in dic.keys():
            if dic[key] == 1:
                res += key
        return res