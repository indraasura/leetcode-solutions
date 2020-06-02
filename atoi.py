class Solution: 
    def __init__(self, s: str) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        res = 0
        i = 0
        negative = 1
        # whitespace check
        while i < len(s) and s[i] == ' ':
            i += 1
        # +/- symbol check : no loop as only one time check
        if i < len(s) and s[i] == '-':
            negative = -1
            i += 1
        if i < len(s) and s[i] == '+':
            i += 1
        # number check
        checker = set('0123456789')
        while i < len(s) and s[i] in checker:
            res = res*10 + int(s[i])
            i += 1
        res = res * negative
        if res < 0:
            return max(res, MIN_INT)
        else:
            return min(res, MAX_INT)