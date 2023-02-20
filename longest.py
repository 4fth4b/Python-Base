a=list(input('Enter a list of strings').split())
max=len(a[0])
for i in a:
    if max<len(i):
        max=len(i)
print(max)
    