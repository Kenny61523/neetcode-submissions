class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # edge case 
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True

        hand.sort()
        res = []

        for n in hand:
            res.append(n)

        while True:
            if len(res) == 0: 
                break
            startIndex = min(res)
            for i in range(startIndex, startIndex + groupSize):
                if i not in res:
                    return False
                res.remove(i)

        return True
