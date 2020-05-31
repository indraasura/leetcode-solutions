class Solution:
    def reverse(self, x: int) -> int:
        res = int((x+0.1)/abs(x+0.1))*int(str(abs(x))[::-1])
        return res if -2**31 < res < 2**31-1 else 0
