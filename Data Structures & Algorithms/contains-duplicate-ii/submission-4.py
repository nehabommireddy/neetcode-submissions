class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        first = 0
        second = 1
        s = set()
        s.add(nums[first])
        while second < len(nums):
            if second - first > k:
                s.remove(nums[first])
                first += 1
            if nums[second] in s:
                return True
            s.add(nums[second])
            second += 1
        return False

        