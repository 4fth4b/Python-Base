a=int (input('Enter the value of a'))
b=int (input('Enter the value of b'))
c=int (input('Enter the value of c'))
if a>b and b>c:
    print('A is greater')
elif b>c and c>a:
    print('B is greater')
else:
    print('C is greater')         