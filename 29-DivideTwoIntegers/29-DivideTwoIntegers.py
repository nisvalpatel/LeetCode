# Last updated: 7/10/2025, 11:58:24 AM
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ANS_MAX = 2**31 - 1
        ANS_MIN = -2**31
        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            temp = divisor
            multiplier = 1
            while dividend >= temp * 2:
                temp *= 2
                multiplier *= 2
            dividend -= temp
            count += multiplier
            
        return max(ANS_MIN, min(ANS_MAX, sign * count))