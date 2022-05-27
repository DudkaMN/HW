from itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i ** 2)
my_list = []
for el in cycle(["один", "два", "три"]):
    if my_list.count(el) < 2:
        my_list.append(el)
    else:
        break
for ind, el in enumerate(my_list, 1):
    print(ind, el)

