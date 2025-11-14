class Solution(object):
  def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        res = []
        count = 1
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == s[i+1]:
                count += 1
            else:
                res.append(str(count))
                res.append(s[i])
                count = 1
        s = "".join(res)
    return s