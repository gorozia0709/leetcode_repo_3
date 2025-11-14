class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    num_map = {num: i for i, num in enumerate(nums)}
    for i, num in enumerate(nums):
      complement = target - num
      if complement in num_map and num_map[complement] != i:
        return [i, num_map[complement]]