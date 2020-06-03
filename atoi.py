class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0 
        res = 0
        count = 0
        negative = 1
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        # whitespace check
        while i < len(str) and str[i] == ' ':
            i += 1
        # +/i check
        if i < len(str) and str[i] == '-':
            negative = -1
            i += 1
            count += 1
        if i < len(str) and str[i] == '+':
            i += 1
            count += 1
        if count > 1:
            return 0
        else: 
        # number check
            checker = set('0123456789')
            while i < len(str) and str[i] in checker:
                res = res*10 + int(str[i])
                i += 1
            res *= negative
            if res < 0:
                return max(res, MIN_INT)
            else:
                return min(res, MAX_INT)
        