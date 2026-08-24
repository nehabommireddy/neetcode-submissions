class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_freq = {}
        for num in nums:
            dict_freq[num] = dict_freq.get(num,0) + 1
            
        arr_freq = []
        for num, count in dict_freq.items():
            arr_freq.append([count, num])

        arr_freq.sort()

        result = []
        for i in range (0,k):
            result.append(arr_freq.pop()[1])
        
        return result
        