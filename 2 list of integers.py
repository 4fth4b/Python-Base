x=[]
y=[]
i=0
j=0
n=int(input('Enter the number of elements of list 1:'))
print('Enter the numbers of list 1:')
for i in range(i,n):
    b=int(input())
    x.append(b)
print('the list 1 is:',x)   
m=int(input('Enter the number of elements of list 2:'))
print('Enter the numbers of list 2:')
for i in range(j,m):
    c=int(input())
    y.append(c)
print('the list 2 is:',y)   
if len(x)==len(y):
    print('the length of the lists are same.')
else:
    print('the length of the lists are not same.')   
sumx=sum(x)
sumy=sum(y)
if sumx==sumy:
    print(f'sum of list 1: {sumx} is equal to sum of list 2: {sumy}')
else:
    print(f'sum of list 1: {sumx} is not equal to sum of list 2: {sumy}')
for i in range(i,n):
    for j in range(j,m):
        if x[i]==y[j]:
            d=x[i]
            print(f'the common number is',d)
if d==0:
    print('there are no common numbers in these lists')
  
