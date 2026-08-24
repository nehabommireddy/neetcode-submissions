class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        j = 1
        k = len(nums) - 1
        result = []

        for i in range (len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < k:
                if (nums[j] + nums[k]) == -(nums[i]):
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                elif (nums[j] + nums[k]) < -nums[i]:
                    j += 1
                else:
                    k -= 1
        
        result = [list(x) for x in set(tuple(x) for x in result)]

        return result
        