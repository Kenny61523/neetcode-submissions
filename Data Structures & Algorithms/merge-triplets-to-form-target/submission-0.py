class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # greedy 
        # filter out triplets
        for n in triplets:
            if n[0] > target[0] or n[1] > target[1] or n[2] > target[2]:
                triplets.remove(n)


        bool1 = False
        bool2 = False
        bool3 = False
        # check if you can find in any tripletes all three numbers
        for n in triplets:
            if n[0] == target[0]:
                bool1 = True
            if n[1] == target[1]:
                bool2 = True
            if n[2] == target[2]:
                bool3 = True

        return bool1 and bool2 and bool3
                