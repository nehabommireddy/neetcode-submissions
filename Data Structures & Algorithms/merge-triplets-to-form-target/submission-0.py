class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []
        for x,y,z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                valid.append([x,y,z])
        t1 = False
        t2 = False
        t3 = False
        for x,y,z in valid:
            if x == target[0]:
                t1 = True
            if y == target[1]:
                t2 = True
            if z == target[2]:
                t3 = True
        
        if t1 and t2 and t3:
            return True
        else:
            return False