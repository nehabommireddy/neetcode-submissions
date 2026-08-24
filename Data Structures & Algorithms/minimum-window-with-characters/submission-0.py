class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isValid(dict1, dict2):
            valid = True
            for key in dict1.keys():
                if dict2.get(key,0) < dict1[key]:
                    valid = False
            return valid

        dict1 = {}
        answer = None
        for char in t:
            dict1[char] = dict1.get(char, 0) + 1

        left = 0
        dict2 = {}
        for right in range(len(s)):
            dict2[s[right]] = dict2.get(s[right], 0) + 1

            while isValid(dict1, dict2):
                new = s[left:right+1]
                if answer is None or len(new) < len(answer):
                    answer = new
                dict2[s[left]] = dict2.get(s[left],0) - 1
                left += 1
        
        if answer == None:
            return ""
        else:
            return answer


            
            
            



        