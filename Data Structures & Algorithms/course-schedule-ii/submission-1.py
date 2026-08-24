class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        result = []
        
        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(result) != numCourses:
            return []
        return result
