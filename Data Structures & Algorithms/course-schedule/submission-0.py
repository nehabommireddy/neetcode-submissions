class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        visited = set()
        graph = {i: [] for i in range(numCourses)}

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            visited.add(course)
            return True
        
        for p in prerequisites:
            graph[p[1]].append(p[0])
        
        for course in graph:
            if dfs(course) == False:
                return False
        
        return True
           
        

        