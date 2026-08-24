class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        num = ""
        number = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
            if s[i] == "#":
                number = int(num)
                num = ""
                res.append(s[i+1:i+number+1])
                i += number
            i+= 1
        return res
            
