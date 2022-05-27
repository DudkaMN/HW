ls = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
mls = [ls[i + 1] for i in range(len(ls) - 1) if ls[i + 1] > ls[i]]
print(mls)
