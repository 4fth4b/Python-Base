list1=list(input('Enter the colors for list 1: ').split())
list2=list(input('Enter the colors for list 2: ').split())
b=set(list1).intersection(list2)
c=set(list1)-b
print('colors in list1 not in list2: ',c)