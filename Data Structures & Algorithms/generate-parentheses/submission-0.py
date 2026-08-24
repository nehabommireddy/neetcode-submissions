class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        def backtracking(o, c, path):
            if c > o:
                return
            if o > n:
                return
            if c > n: 
                return
            
            if c+o == 2*n:
                result.append(path[:])
            
            backtracking(o+1, c, path + "(")
            if c < o:
                backtracking(o, c+1, path+")")
        backtracking(0, 0, "")
        return result