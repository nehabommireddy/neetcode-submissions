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
                else:
                    if stars:
                        stars.pop()
                    else:
                        return False
        
        while left and stars:
            l = left.pop()
            s = stars.pop()
            if (l>s):
                return False
        
        if left:
            return False
        return True
        
        