class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for (i,t) in enumerate(temperatures):
            if not stack: 
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < t:
                    index = stack.pop()
                    res[index] = i-index
                stack.append(i)
        
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """res = [0] * len(temperatures)
        stack = []
        for i in range (len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                res[index] = i-index
            stack.append(i)
        
        return res"""

        