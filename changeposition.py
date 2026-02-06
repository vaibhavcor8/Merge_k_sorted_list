nums=[0,0,0,3,0,5,0,6,0,9]
pos=0
for n in nums:
    if n!=0:
        nums[pos]=n
        pos+=1

for i in range(pos,len(nums)):
    nums[i]=0
print(nums)