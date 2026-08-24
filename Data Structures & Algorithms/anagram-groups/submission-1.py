class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = [0] * 26
        dic = {}
        for st in strs:
            for char in st:
                arr[ord(char) - ord("a")] += 1
            key = tuple(arr)
            if key not in dic:
                dic[key] = []
            dic[key].append(st)
            arr = [0] * 26
        return list(dic.values())
            
        