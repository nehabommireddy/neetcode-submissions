class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''res = [1] * len(nums)
        prefix = [1]* len(nums)
        suffix = [1]* len(nums)

        for i in range (1,len(nums)):
            prefix[i] = prefix [i-1] * nums[i-1]
        for i in range (len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range (len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res'''
        total = 1
        res = [1] * len(nums)
        zero = 0
        for num in nums:
            if num: 
                total = total * num
            else:
                zero += 1
        if zero >= 2:
            return [0] * len(nums)
        for i in range (len(nums)):
            if zero == 1:
                if nums[i] != 0:
                    res[i] = 0
                else:
                    res[i] = total
            else:
                res[i] = total//nums[i]

        return res