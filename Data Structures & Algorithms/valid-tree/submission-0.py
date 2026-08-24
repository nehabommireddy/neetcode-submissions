class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(edge, parent):
            if edge in visited:
                return False
            visited.add(edge)
            for e in graph[edge]:
                if e != parent:
                    if not dfs(e, edge):
                        return False
            
            return True
        
        if not dfs(0,-1):
            return False
        
        if len(visited) != len(graph):
            return False

        return True



        