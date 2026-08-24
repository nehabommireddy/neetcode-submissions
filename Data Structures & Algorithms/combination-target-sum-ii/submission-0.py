class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []

        def backtracking (i, path):
            if sum(path) == target:
                combinations.append(path[:])
                return
            if sum(path) > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                path.append(candidates[j])
                backtracking(j + 1, path)
                path.pop()
        
        backtracking(0,[])
        return combinations
