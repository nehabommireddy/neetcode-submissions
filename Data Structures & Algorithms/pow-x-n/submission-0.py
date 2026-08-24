class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = False
        if n < 0:
            neg = True
            n = -n
        
        def pow(x,n):
            odd = False
            if n == 0:
                return 1
            if x== 0:
                return 0
            if n%2 != 0:
                odd = True
            half = pow(x, n//2)
            result = half*half

            if odd:
                result *= x
            return result
        res = pow(x,n)
        if neg:
            return 1/res
        else:
            return res
        