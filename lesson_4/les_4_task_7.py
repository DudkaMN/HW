def fact(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
        i += 1
        yield fact


for el in fact(50):
    print(el)
