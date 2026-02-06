num=[1,2,3,4,5]
even_square=[]
res=0
for x in num:
    if x%2==0:
        res=x*x
        even_square.append(res)
print(even_square)