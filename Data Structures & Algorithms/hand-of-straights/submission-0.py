class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        dic = {}

        for h in hand:
            dic[h] = dic.get(h,0) + 1
    
        for card in hand:
            if (dic.get(card,0) == 0):
                continue

            for i in range (groupSize):
                if (dic.get(card+i,0) > 0):
                    dic[card+i] -= 1
                else: 
                    return False

        return True