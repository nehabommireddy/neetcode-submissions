class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(num):
            sum = 0
            while num:
                digit = num % 10
                num = num // 10
                sum += digit**2
            return sum
        
        seen = set()
        while n != 1:
            n = helper(n)
            if n in seen:
                return False
            seen.add(n)
        
        return True