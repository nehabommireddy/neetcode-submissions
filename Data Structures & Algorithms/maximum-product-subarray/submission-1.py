class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        result = nums[0]
        for num in nums[1:]:
            oldMax = currMax
            oldMin = currMin
            currMax = max(num, num*oldMax, num*oldMin)
            currMin = min(num, num*oldMax, num*oldMin)
            result = max(result, currMax)

        return result