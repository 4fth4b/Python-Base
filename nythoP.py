a="Python"
b=list(a)
b.remove('P')
b.remove('n')
b.append('P')
b.insert(0,'n')
print(b)
c=""
for i in b:
    c+=i
print(c)