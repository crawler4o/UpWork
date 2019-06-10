x = {'both1': 1, 'both2': 2, 'only_x': 100}
y = {'both1': 10, 'both2': 20, 'only_y': 200}

print({k: x.get(k, 0) + y.get(k, 0) for k in set(x)})
print({k: x.get(k, 0) + y.get(k, 0) for k in set(x) & set(y)})
print({k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y)})
print({k: x.get(k, 0) + y.get(k, 0) for k in set(x) ^ set(y)})
