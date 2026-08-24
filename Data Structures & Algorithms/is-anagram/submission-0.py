class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False;
        letter_s = {}
        letter_t = {}
        for i in range (len(s)):
            letter_s[s[i]] = 1 + letter_s.get(s[i], 0)
            letter_t[t[i]] = 1 + letter_t.get(t[i], 0)
        
        if (letter_s == letter_t): 
            return True
        else:
            return False