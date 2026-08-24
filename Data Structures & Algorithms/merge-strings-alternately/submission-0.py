class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = []
        for i in range(min(len(word1), len(word2))):
            arr.append(word1[i])
            arr.append(word2[i])
        
        for j in range (min(len(word1), len(word2)), len(word1)):
            arr.append(word1[j])

        for j in range (min(len(word1), len(word2)), len(word2)):
            arr.append(word2[j])
        
        return "".join(arr)