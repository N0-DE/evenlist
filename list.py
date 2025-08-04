l1=[]
l=list(eval(input("Enter a list")))
for i in l:
    if (i%2==0):
        l1.append(i)
print('New list')
print(l1)