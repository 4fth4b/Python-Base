# a=list(input('Enter a string: '))
# if a[-1]=='g' and a[-2]=='n' and a[-3]=='i':
#     a.remove(a[-3])
#     a[-2]='l'
#     a[-1]='y'
#     print(a)
# else:
#     a.append('ing')
#     print(a)      

b='ing'
a=(input('Enter a string: '))
if a[-3:]=='ing':
    a=a.replace(a[-3:],'ly')
    print(a)
else:
    a=a+b
    print(a)
