class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    
    INT_MIN, INT_MAX = -2147483648, 2147483647

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    for i in range(31, -1, -1):
        if (dividend >> i) >= divisor:
            dividend -= (divisor << i)
            quotient += (1 << i)

    return -quotient if negative else quotient