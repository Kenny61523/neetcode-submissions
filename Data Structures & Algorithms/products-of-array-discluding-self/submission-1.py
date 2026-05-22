class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        sum = 1
        zeroCnt = 0

        for n in nums:
            if n == 0: 
                zeroCnt += 1
                if zeroCnt > 1: 
                    sum = 0 
                    break
                else: 
                    continue
            sum *= n
                
        print(sum)
        val = sum 
        for n in nums:
            if zeroCnt == 1:
                if n == 0:
                    res.append(int(sum))
                    print(sum)
                else: 
                    res.append(0)
                continue
            
            if n != 0: val = sum / n
            res.append(int(val))

        return res