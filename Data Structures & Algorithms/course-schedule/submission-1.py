class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        visited = set()
        a = [[] for _ in range(numCourses)]
        for p in prerequisites:
            a[p[1]].append(p[0])

        
        def dfs(i):
            if i in path:
                return False
            if i in visited:
                return True
            
            path.add(i)
            visited.add(i)
            b = True
            for n in a[i]:
                b = b and dfs(n)
            path.remove(i)
            return b
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        
        return True
        
        