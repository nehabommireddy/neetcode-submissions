class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []

        for i, char in enumerate(s):
            if char == "(":
                left.append(i)
            if char == "*":
                stars.append(i)
            if char == ")":
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while left and stars:
            if left.pop() > stars.pop():
                return False
        
        return not left
        
        