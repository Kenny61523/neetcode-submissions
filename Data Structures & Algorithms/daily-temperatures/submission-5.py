class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # nend a way to store the temp
        # have a list that stores the tmp and index
        # initialize result list with [0]

        # iterate throguh the array with pointer i
            # if the temp is lower pop from stack 
                # store i - j on res[i]
            
            # append to stack [tmp, index]
        # return res

        # Input: temperatures = [30,38,30,36,42,40,28]

        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                tmp, index = stack.pop()
                res[index] = i - index

            stack.append([temperatures[i], i])

        return res
            


