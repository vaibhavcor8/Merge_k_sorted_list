from typing import List
class Solution:
    def fun(self, nums:List[int], target:int)->List[int]:
        prevMap={}
        for i,n in enumerate(nums):
            diff= target-n
            if diff in prevMap:
                return (prevMap[diff],i)
            prevMap[n]=i

sol=Solution()
print(sol.fun([8,5,7,9,4],12))