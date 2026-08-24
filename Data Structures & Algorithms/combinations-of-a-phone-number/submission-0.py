class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {}
        if not digits:
            return []
        dic["2"] = ["a","b","c"]
        dic["3"] = ["d","e","f"]
        dic["4"] = ["g","h","i"]
        dic["5"] = ["j","k","l"]
        dic["6"] = ["m","n","o"]
        dic["7"] = ["p","q","r","s"]
        dic["8"] = ["t","u","v"]
        dic["9"] = ["w","x","y","z"]
        result = []

        def backtracking(i,path):
            if i >= len(digits):
                result.append("".join(path))
                return
            
            for val in dic[digits[i]]:
                path.append(val)
                backtracking(i+1, path)
                path.pop()

        backtracking(0,[])
        return result
            
