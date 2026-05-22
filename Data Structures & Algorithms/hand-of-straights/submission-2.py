from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # edge case 
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True

        res = defaultdict(int)

        for n in hand:
            res[n] += 1

        print(res)

        minH = list(res.keys())
        heapq.heapify(minH)

        while minH:
            minIndex = minH[0]
            for i in range(minIndex, minIndex + groupSize):
                if i not in minH:
                    return False
                res[i] -= 1
                if res[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
