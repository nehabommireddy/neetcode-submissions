class Solution:
    def isValid(self, s: str) -> bool:
        paren = {}
        paren[")"] = "("
        paren["}"] = "{"
        paren["]"] = "["
        stack = []

        for char in s:
            if char in paren.values():
                stack.append(char)
            if char in paren.keys():
                if not stack:
                    return False
                if stack.pop() != paren[char]:
                    return False
        
        if not stack:
            return True
        return False


















        """my_dict = {}
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
        
        return True"""