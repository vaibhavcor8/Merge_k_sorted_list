# nums=[1,2,3,2,1,5,6,5]
# dic={}
# for n in nums:
#     if n in dic:
#         dic[n]+=1
#     else:
#         dic[n]=1
# print(dic)
# for i in dic:
#     if dic[i]>1:
#         print(i)


nums=[1,2,3,2,1,5,6,5]
previous=set()
duplicates=set()
for n in nums:
    if n in previous:
        duplicates.add(n)
    else:
        previous.add(n)
print(list(duplicates))