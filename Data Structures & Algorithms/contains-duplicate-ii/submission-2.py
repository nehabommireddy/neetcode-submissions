class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        first = 0
        second = 1
        dic = {}
        dic[first] = nums[first]
        while second < len(nums):
            if second - first > k:
                del dic[first]
                first += 1
            if nums[second] in dic.values():
                return True
            dic[second] = nums[second]
            second += 1
        return False

        