class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range (len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)
        stack = []
        count = 0
        for (pos, speed) in cars:
            time =(target-pos)/speed
            if stack and time > stack[-1]:
                stack.append(time)
            if not stack: 
                stack.append(time)
        
        return len(stack)




























        """cars = []
        for i in range (len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        times = [0] * len(position)
        for i in range (len(cars)):
            times[i] = (target-cars[i][0])/cars[i][1]
        
        stack = [times[0]]
        for i in range (1,len(times)):
            if (times[i] > stack[-1]):
                stack.append(times[i])

        return len(stack)"""




        