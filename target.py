from typing import List
class Solution:
    def fun(self, nums:List[int],target:int)->List[int]:
        n=len(nums)
        for i in range (n):
            for j in range (i+1,n):
                if nums[i]+nums[j] == target:
                        return[i,j]
                
            
sol=Solution()

mynums=[8,5,7,9,4]
my_target=12
result=sol.fun(mynums,my_target)
print(result)
