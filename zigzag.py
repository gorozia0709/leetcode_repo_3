class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
      
    n = len(s)
    cycle_len = 2 * numRows - 2
    result = []
    
    for i in range(numRows):
      for j in range(0, n - i, cycle_len):
        result.append(s[j + i])
        if 0 < i < numRows - 1:
          second_idx = j + cycle_len - i
          if second_idx < n:
            result.append(s[second_idx])
            
    return "".join(result)