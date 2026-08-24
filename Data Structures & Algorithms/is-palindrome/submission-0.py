class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = ''.join(char for char in s if char.isalnum())
        for i in range (len(chars)//2):
            if not ((chars[i]).lower() == (chars[len(chars)-i-1]).lower()):
                return False
        return True