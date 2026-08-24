class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals_seen = set()
        for i in nums:
            if i in vals_seen:
                return True
            vals_seen.add(i)
        return False
        