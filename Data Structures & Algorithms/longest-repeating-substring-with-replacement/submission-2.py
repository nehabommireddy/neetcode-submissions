class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        if (len(s) == 0):
            return 0
        length = 1
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            window = right - left + 1
            most = max(freq.values())
            while window-most > k:
                freq[s[left]] -= 1
                left += 1
                window = right - left + 1
                most = max(freq.values())
            
            length = max(length, window)
        
        return length

        