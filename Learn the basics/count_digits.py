class Solution:
    def countDigit(self, n):
        dig = 0
        while n > 0:
            n = n/10
            n = round(n)
            dig += 1
        return dig
