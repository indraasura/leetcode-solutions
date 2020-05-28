class Solution:
    def longestPalindrome(self, input_string: str) -> str:
        if len(input_string) == 1:
            return input_string
        m = []
        for i in range(len(input_string)):
            for j in range(i+1, len(input_string)+1):
                substring = input_string[i:j]
                if substring == substring[::-1] and len(substring) >= len(m):
                    m = substring
        output = ''.join(m)
        return output
                
                
            