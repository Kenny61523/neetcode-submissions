class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy 
        if sum(gas) - sum(cost) < 0:
            return -1


        start = 0
        cur = 0
        for i in range(len(gas)):
                cur += gas[i] - cost[i] 
                # route cannot be taken
                if cur < 0:
                    cur = 0
                    start = i + 1        
                
        return start
