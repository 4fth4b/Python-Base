list1=['a','b','c','d']
list2=['e','f']
for i in list1:
    list2.append(i)
print(list2)
dict1={"Brand":"Honda","year":2022,"model":"city"}
dict2={"car":"swift","bike":"cb"}
for i in dict2:
    dict1[i]=dict2[i]
print(dict1)    
n=0
while(n<=10):
   print(n)
   n+=1
a=50
b=50
if(a>b):
    print('A is greater')
elif(b>a):
    print('B is greater')   
else:
    print('both are equal')
     