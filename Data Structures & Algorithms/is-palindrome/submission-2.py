"""chars = ''.join(char for char in s if char.isalnum())
        for i in range (len(chars)//2):
            if not ((chars[i]).lower() == (chars[len(chars)-i-1]).lower()):
                return False
        return True"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ""
        for char in s:
            if char.isalnum():
                l += char.lower()
        
        for i in range(len(l)//2):
            if l[i] != l[len(l)-i-1]:
                return False
        
        return True