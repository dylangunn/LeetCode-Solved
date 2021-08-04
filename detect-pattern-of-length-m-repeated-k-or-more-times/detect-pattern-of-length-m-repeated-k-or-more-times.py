class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m * k > len(arr): return False
        mCheck = 0
        for i in range(0, len(arr) - m*k + 1):
            curr = True
            for j in range(i,i+m):
                num = arr[j]
                for l in range(k):
                    if arr[j+m*l] != num:
                        curr = False
                        break
                if not curr:
                    break
                if j == i + m - 1:
                    return True
        return False
                    