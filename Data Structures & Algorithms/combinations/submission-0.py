class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(i):
            if len(path) == k and i <= n+1:
                res.append(path.copy())
                return
            if i > n or len(path) > k:
                return
            
            path.append(i)
            backtracking(i+1)
            path.pop()
            backtracking(i+1)
            return
        
        backtracking(1)
        return res
            

        