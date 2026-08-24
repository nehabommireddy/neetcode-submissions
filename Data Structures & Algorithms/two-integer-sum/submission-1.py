class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        dic = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in dic:
                res.append(dic[complement])
                res.append(i)
                break
            dic[n] = i
        
        return res
