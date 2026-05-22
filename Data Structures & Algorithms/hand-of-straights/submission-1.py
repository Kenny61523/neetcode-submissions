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

        while True:
            if len(res) == 0: 
                break

            minIndex = min(res.keys())
            print(f"minINdex={minIndex}")
            for i in range(minIndex, minIndex + groupSize):
                if res[i] == 0:
                    return False
                res[i] -= 1
                if res[i] == 0:
                    del res[i]

        return True
