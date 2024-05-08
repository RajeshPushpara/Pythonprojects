l=[1,2,3,4,56,78,90]
even=[]
odd=[]
for i in l:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Even elements:",even)
print("Odd elements:",odd)