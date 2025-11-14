import re

class Solution:
  def myAtoi(self, s: str) -> int:
    match = re.match(r'^\s*([+-]?\d+)', s)
    
    if not match:
      return 0
      
    num_str = match.group(1)
    num = int(num_str)
    
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    if num < INT_MIN:
      return INT_MIN
    if num > INT_MAX:
      return INT_MAX
      
    return num