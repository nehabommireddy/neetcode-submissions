class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {}
        my_dict[")"] = "(" 
        my_dict["}"] = "{"
        my_dict["]"] = "[" 
        stack = []

        for char in s:
            if char in my_dict.values():
                stack.append(char)
            elif char in my_dict.keys():
                if not stack or stack.pop() != my_dict[char]:
                    return False
        
        if stack:
            return False
        
        return True