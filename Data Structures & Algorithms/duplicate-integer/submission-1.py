class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        compare = set(nums)
        if len(compare) == len(nums):
            return False
        return True
        