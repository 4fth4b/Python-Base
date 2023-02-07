a=list(input('Enter the names:').split())
print("the list of names:",a)
i=0
m=0
n=len(a)
for i in range(i,n):
    b=[i for a,i in enumerate(a[i]) ]
    p=len(b)
    for i in range(i,p):
        if b[i]=='a':
            m+=1 
print('the number of a in the given list of names is:',m)    