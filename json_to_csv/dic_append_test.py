a = {1: 'a', 2: 'b', 3: 'c'}

b = {4: 'd', 3: 'e', 4: 'f'}
out1 = []
out2 = []


out1.append(a)
out2.append({**a})

print(out1)
print(out2)