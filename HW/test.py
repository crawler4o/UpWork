a = {'asd':1, 'qwer':2, 'tyui':0, 'zxcv':2, 'sdfg':2}
b = {'asd':1, 'qwer':1, 'tyui':1}




print(set(a).difference(b))

for x in a.keys():
    if 'as' in x:
        a['new'] = a.pop(x)
print(a)