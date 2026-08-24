class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result1 = 0
        for num in nums:
            result1 = result1 ^ num

        result2 = 0
        for i in range (0, len(nums)+1):
            result2 = result2 ^ i
        
        return result1 ^ result2
        