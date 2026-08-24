class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        count = n
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        for i,j in edges:
            rooti = find(i)
            rootj = find(j)
            if rooti != rootj:
                par[rootj] = rooti
                count -= 1
        
        return count

        