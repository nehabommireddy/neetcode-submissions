"""chars = ''.join(char for char in s if char.isalnum())
        for i in range (len(chars)//2):
            if not ((chars[i]).lower() == (chars[len(chars)-i-1]).lower()):
                return False
        return True"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for char in s:
            if char.isalnum():
                arr.append(char.lower())
        
        for i in range(len(arr)//2):
            if arr[i] != arr[len(arr)-1-i]:
                return False
        
        return True

        