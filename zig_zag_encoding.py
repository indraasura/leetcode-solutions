class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        
        row = 0 
        res = [[] for x in range(numRows)]
        delta = -1
        for c in s:
            res[row].append(c)
            if row == 0 or row == numRows - 1:
                delta *= -1
            row += delta
        for x in range(len(res)):
            res[x] = ''.join(res[x])
        return ''.join(res)