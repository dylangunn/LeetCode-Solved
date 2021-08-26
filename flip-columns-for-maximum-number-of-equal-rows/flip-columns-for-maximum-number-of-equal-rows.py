class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        uniq = {}
        cols = len(matrix[0])
        for i in range(len(matrix)):
            cur = 0
            if matrix[i][0] == 1:
                for j in range(cols):
                    cur += pow(2 * (matrix[i][j] ^ 1),j)
            else:
                for j in range(cols):
                    cur += pow(2 * matrix[i][j],j)
            if cur in uniq:
                uniq[cur] += 1
            else:
                uniq[cur] = 1
        return max(uniq.values())
                
                    
            