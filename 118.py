class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        if numRows == 1: return out
        for i in range(1,numRows):
            x = [0]+out[i-1]
            for j in range(i):
                x[j] = x[j]+x[j+1]
            out.append(x)
        return out
