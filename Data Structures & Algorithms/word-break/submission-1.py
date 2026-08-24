class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i < 0:
                return True

            if i in memo:
                return memo[i]

            for word in wordDict:
                if i-len(word)+1 >= 0 and s[i-len(word)+1:i+1] == word:
                    if dfs(i-len(word)):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False
        
        return dfs(len(s)-1)

        