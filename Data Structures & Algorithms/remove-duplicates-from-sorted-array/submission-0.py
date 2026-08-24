class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        seen = set()
        unique = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[unique] = nums[i]
                unique += 1
        
        return unique