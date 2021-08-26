class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        res1 = []
        res2 = []
        for c in s1:
            res1.append(c)
        for c in s2:
            res2.append(c)
        res1.sort()
        res2.sort()
        
        big1 = 1
        big2 = 1
        for i in range(len(s1)):
            if big1 and res1[i] < res2[i]:
                big1 = 0
            if big2 and res1[i] > res2[i]:
                big2 = 0
            if not (big1 or big2):
                return False
        return True