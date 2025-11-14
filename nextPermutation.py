from itertools import permutations

class Solution:
  def nextPermutation(self, nums: list[int]) -> None:
    if not nums:
        return
    
    original_tuple = tuple(nums)
    
    all_perms = sorted(list(set(permutations(nums))))
    
    current_index = all_perms.index(original_tuple)
    
    next_index = (current_index + 1) % len(all_perms)
    
    next_perm = all_perms[next_index]
    
    for i in range(len(nums)):
        nums[i] = next_perm[i]